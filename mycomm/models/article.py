from django.db import models

from mycomm.models.user import User
from mycomm.models.board import Board


class Article(models.Model):
    ARTICLE_TYPE = [
        ('NOTICE', 'notice'),
        ('NORMAL', 'normal'),
        ('PICTURE', 'picture'),
        ('CALENDER', 'calender'),
    ]
    title = models.CharField(
        verbose_name='제목',
        max_length=255,
        null=False,
        blank=False
    )
    content = models.TextField(
        verbose_name='내용',
        null=False,
        blank=True
    )
    type = models.CharField(
        verbose_name='종류',
        choices=ARTICLE_TYPE,
        default='NORMAL',
        null=False,
        blank=False
    )
    writer = models.ForeignKey(
        verbose_name='작성자',
        to=User,
        on_delete=models.SET_NULL,
        null=False,
        related_name='writer_article'
    )
    board = models.ForeignKey(
        verbose_name='게시판',
        to=Board,
        on_delete=models.CASCADE,
        null=False,
        related_name='board_article'
    )
    like_by = models.ManyToManyField(
        verbose_name='좋아요 선택 유저',
        to=User,
        null=True,
        related_name='likeby_article'
    )
