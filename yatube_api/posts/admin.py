from django.contrib import admin

from posts.models import Group, Post, Follow, Comment
from posts.mixins import AdminFieldLinkMixin


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'description')
    search_fields = ('title', 'slug')


@admin.register(Post)
class PostAdmin(AdminFieldLinkMixin, admin.ModelAdmin):
    list_display = ('text', 'author_link', 'group', 'group_link', 'pub_date')
    search_fields = ('text', 'author__username')
    list_filter = ('group', )

    def author_link(self, obj):
        author = obj.author
        return self._get_object_link_html(author, author.username)

    def group_link(self, obj):
        if obj.group:
            group = obj.group
            return self._get_object_link_html(group, group.title)


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ('user', 'following', 'follow_date')
    search_fields = ('user__username',)


@admin.register(Comment)
class CommentAdmin(AdminFieldLinkMixin, admin.ModelAdmin):
    list_display = ('text', 'author', 'post_link', 'created')
    search_fields = ('author__username', 'post__text', 'post__id')

    def post_link(self, obj):
        post = obj.post
        return self._get_object_link_html(post, post.text)
