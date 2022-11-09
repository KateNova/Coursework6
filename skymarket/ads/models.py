from django.conf import settings
from django.core.validators import MinLengthValidator
from django.db import models


class Ad(models.Model):
    title = models.CharField(
        max_length=200,
        validators=[
            MinLengthValidator(8),
        ],
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='ads'
    )
    price = models.PositiveIntegerField()
    description = models.CharField(max_length=1000, null=True, blank=True)
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    image = models.ImageField(upload_to='ad/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        ordering = ('-created_at',)


class Comment(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    text = models.CharField(
        max_length=1000,
        validators=[
            MinLengthValidator(8),
        ],
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    ad = models.ForeignKey(
        Ad,
        on_delete=models.CASCADE,
        related_name='comments'
    )

    def __str__(self):
        return self.text[:50]

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ('-created_at',)
