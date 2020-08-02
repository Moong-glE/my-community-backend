from django.db import models

from mycomm.models.article import Article


class Vote(models.Model):
    article = models.OneToOneField(
        verbose_name='게시글',
        to=Article,
        on_delete=models.CASCADE,
        null=False
    )

    question = models.CharField(
        verbose_name='제목',
        max_length=255,
        null=False,
        blank = False
    )

    expired_at = models.DateTimeField(
        verbose_name='만료 일시',
        null=False
    )

    is_expired = models.BooleanField(
        verbose_name='만료 여부',
        null=False,
        default=False
    )

    answer_item_list = models.ListCharField(
        verbose_name='항목 리스트',
        max_length=255,
        null=False
    )
