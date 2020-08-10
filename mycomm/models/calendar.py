from django.db import models

from mycomm.models.article import Article


class Calendar(models.Model):
    description = models.CharField(
        verbose_name='내용',
        max_length=100,
        null=False,
        blank=False
    )
    start_at = models.DateTimeField(
        verbose_name='시작 시간',
        null=False,
        blank=False
    )
    end_at = models.DateTimeField(
        verbose_name='종료 시간',
        null=False,
        blank=False
    )
    article = models.OneToOneField(
        verbose_name='게시글',
        to=Article,
        on_delete=models.CASCADE,
        null=False,
        related_name='article_calendar'
    )
