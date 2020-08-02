from django.db import models

from mycomm.models.user import User
from mycomm.models.vote import Vote

class VoteAnswer(models.Model):
    user = models.OneToOneField(
        verbose_name='투표에 답변한 사용자 ID',
        to=User,
        on_delete=models.CASCADE,
        null=False
    )

    vote = models.OneToOneField(
        verbose_name='답변에 대한 투표 ID',
        to=Vote,
        on_delete=models.CASCADE,
        null=False
    )

    answers = models.CharField(
        verbose_name='답변들',
        max_length=255,
        null=False
    )