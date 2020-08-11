from django.db import models

from mycomm.models.department import Department
from mycomm.models.user import User


class Group(models.Model):
    name = models.CharField(
        verbose_name="이름",
        max_length=255,
        null=False,
        blank=False
    )

    description = models.CharField(
        verbose_name='내용',
        max_length=255,
        null=False,
        blank=True
    )

    department = models.ForeignKey(
        verbose_name='학과',
        to=Department,
        on_delete=models.CASCADE,
        null=False,
        related_name='department_group'
    )

    manager = models.ForeignKey(
        verbose_name='관리자',
        to=User,
        on_delete=models.SET_NULL,
        null=False,
        related_name='manager_group'
    )
