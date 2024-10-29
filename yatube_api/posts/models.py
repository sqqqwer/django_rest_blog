from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

STR_OUTPUT_LIMIT = 40


class Group(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    class Meta:
        verbose_name = 'группа'
        verbose_name_plural = 'Группы'
        default_related_name = 'groups'

    def __str__(self):
        return self.title[:STR_OUTPUT_LIMIT]


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts/', null=True, blank=True)
    group = models.ForeignKey(
        Group, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'
        default_related_name = 'posts'

    def __str__(self):
        return self.text[:STR_OUTPUT_LIMIT]


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'Комментарии'
        default_related_name = 'comments'

    def __str__(self):
        return self.text[:STR_OUTPUT_LIMIT]


class Follow(models.Model):
    follow_date = models.DateTimeField('Дата подписки', auto_now_add=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='followers')
    following = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='follows')

    class Meta:
        verbose_name = 'подписка'
        verbose_name_plural = 'Подписки'
        constraints = (
            models.UniqueConstraint(
                fields=('user', 'following'),
                name='unique_follow'
            ),
        )

    def __str__(self):
        return f'{self.user}-{self.following}'[:STR_OUTPUT_LIMIT]
