from django.db import models

from mycomm.models.article import Article


class Survey(models.Model):
    expired_at = models.DateTimeField(
        verbose_name='만료 시간',
        null=False,
        blank=False
    )
    is_expired = models.BooleanField(
        verbose_name='만료 여부',
        null=False,
        default=False
    )
    article = models.OneToOneField(
        verbose_name='게시글',
        to=Article,
        on_delete=models.CASCADE,
        null=False,
        related_name='article_survey'
    )
