from django.db import models

from mycomm.models.board import Board
from mycomm.models.department import Department
from mycomm.models.user import User

class Group(models.Model):
    name = models.CharField(
        verbose_name="그룹 이름",
        max_length=255,
        null=False,
        blank=False
    )

    description = models.CharField(
        verbose_name='내용',
        max_length=255,
        null=False,
        blank=True
        # 이거 다른애들 False 로 했던데...
    )

    department = models.ForeignKey(
        verbose_name='학과',
        to=Department,
        on_delete=models.CASCADE,
        null=False,
        related_name='department_group'
    )

    managers = models.ForeignKey(
        verbose_name='관리자 명단',
        to=User,
        on_delete=models.CASCADE,
        null=False,
        related_name='manager_group'
    )