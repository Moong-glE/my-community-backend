from django.db import models

from mycomm.models.article import Article
from mycomm.models.voteanswer import VoteAnswer


class Vote(models.Model):
    article = models.OneToOneField(
        verbose_name='게시글 ID',
        to=Article,
        on_delete=models.CASCADE,
        null=False
    )

    question = models.CharField(
        verbose_name='투표 제목',
        max_length=255,
        null=False
    )

    expiredAt = models.DateTimeField(
        verbose_name='투표 기간 만료 일시',
        auto_now=False,
        auto_now_add=False,
        null=False
    )

    isExpired = models.BooleanField(
        verbose_name='투표 기간 만료 여부',
        null=False
    )

    answerIds = models.ForeignKey(
        verbose_name='투표 답변 ID들',
        to=VoteAnswer,
        on_delete=models.CASCADE,
        null=False,
        realted_name='answers_vote'
    )

    answerItems = models.CharField(
        verbose_name='투표 항목들',
        max_length=255,
        null=False,
    )
