from django.db import models

from mycomm.models.department import Department
from mycomm.models.group import Group
from mycomm.models.user import User


class Board(models.Model):
    name = models.CharField(
        verbose_name='게시판 이름',
        max_length=255,
        null=False,
        blank=False
    )
    is_hidden = models.BooleanField(
        verbose_name='익명 여부',
        null=False,
        default=False
    )

    department = models.ForeignKey(
        verbose_name='학과',
        to=Department,
        on_delete=models.CASCADE,
        null=False,
        related_name='department_board'
    )
    group = models.ForeignKey(
        verbose_name='그룹',
        to=Group,
        on_delete=models.CASCADE,
        null=True,
        related_name='group_board'
    )
    managers = models.ManyToManyField(
        verbose_name='관리자 명단',
        to=User,
        null=False,
        related_name='manager_board'
    )
