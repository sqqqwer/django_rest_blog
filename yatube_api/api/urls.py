from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import (
    CommentViewSet,
    FollowViewSet,
    GroupViewSet,
    PostViewSet
)

v1_router = DefaultRouter()
v1_router.register('posts', PostViewSet, basename='post')
v1_router.register(r'posts/(?P<post_id>\d+)/comments',
                   CommentViewSet, basename='comment')
v1_router.register('groups', GroupViewSet, basename='group')
v1_router.register('follow', FollowViewSet, basename='follow')

v1_urlpattern = [
    path('', include(v1_router.urls)),
    path('', include('djoser.urls.jwt'))
]

urlpatterns = [
    path('v1/', include(v1_urlpattern))
]
