from django.contrib.postgres import fields
from django.db import models

from mycomm.models.user import User
from mycomm.models.vote import Vote


class VoteAnswer(models.Model):
    user = models.OneToOneField(
        verbose_name='답변자',
        to=User,
        on_delete=models.SET_NULL,
        null=False
    )

    vote = models.ForeignKey(
        verbose_name='투표',
        to=Vote,
        on_delete=models.CASCADE,
        null=False
    )

    answer_list = fields.ArrayField(
        verbose_name='답변 리스트',
        base_field=models.CharField(
            max_length=255,
            null=False
        )
    )
