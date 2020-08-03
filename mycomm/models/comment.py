from django.db import models

from mycomm.models.user import User
from mycomm.models.article import Article


class Comment(models.Model):
    content = models.CharField(
        verbose_name='내용',
        max_length=500,
        null=False,
        blank=False
    )
    writer = models.ForeignKey(
        verbose_name='작성자',
        to=User,
        null=False,
        on_delete=models.SET_NULL,
        related_name='user_comment'
    )
    article = models.ForeignKey(
        verbose_name='게시물',
        to=Article,
        null=False,
        on_delete=models.CASCADE,
        related_name='article_comment'
    )
    parent_comment = models.ForeignKey(
        verbose_name='상위 댓글',
        to='self',
        null=True,
        on_delete=models.SET_NULL,
        related_name='parent_comment'
    )
    like_by = models.ManyToManyField(
        verbose_name='좋아요 선택 유저',
        to=User,
        null=True,
        related_name='likeby_comment'
    )
