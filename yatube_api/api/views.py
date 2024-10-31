from rest_framework import filters, mixins, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly

from api.permissions import IsAuthorOrAdminOnly
from api.serializers import (
    CommentSerializer,
    FollowSerializer,
    GroupSerializer,
    PostSerializer
)
from posts.models import Group, Post


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'post_id'
    permission_classes = (IsAuthenticatedOrReadOnly, IsAuthorOrAdminOnly)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'group_id'
    permission_classes = (AllowAny,)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'comment_id'
    post_url_kwarg = 'post_id'
    permission_classes = (IsAuthenticatedOrReadOnly, IsAuthorOrAdminOnly)

    def get_queryset(self):
        post = self._get_post()
        queryset = post.comments.all()
        return queryset

    def perform_create(self, serializer):
        post = self._get_post()
        serializer.save(
            author=self.request.user,
            post=post
        )

    def _get_post(self):
        post_id = self.kwargs.get(self.post_url_kwarg)
        return get_object_or_404(Post, id=post_id)


class FollowViewSet(
    mixins.CreateModelMixin, mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    serializer_class = FollowSerializer

    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        return self.request.user.follows.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
