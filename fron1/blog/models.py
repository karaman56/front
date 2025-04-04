from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField("Заголовок", max_length=200)
    text = models.TextField("Текст")
    slug = models.SlugField(unique=True)
    image = models.ImageField("Картинка")
    published_at = models.DateTimeField("Дата и время публикации")

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Автор",
        limit_choices_to={'is_staff': True}
    )
    likes = models.ManyToManyField(
        User,
        related_name="liked_posts",
        verbose_name="Кто лайкнул",
        blank=True
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.slug])  # Исправлено здесь

    class Meta:
        ordering = ['-published_at']
        verbose_name = 'пост'
        verbose_name_plural = 'посты'


class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, verbose_name="Пост")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    text = models.TextField("Текст комментария")
    published_at = models.DateTimeField("Дата и время публикации", auto_now_add=True)

    def __str__(self):
        return f"{self.author.username} - {self.text[:20]}"

    class Meta:
        ordering = ['published_at']
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарии'
