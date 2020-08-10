from django.contrib.auth.models import AbstractUser
from django.db import models

from mycomm.models.department import Department


class User(AbstractUser):
    email = models.EmailField(
        verbose_name='이메일',
        max_length=255,
        null=False,
        blank=False,
        unique=True
    )
    student_id = models.CharField(
        verbose_name='학번',
        max_length=100,
        null=True,
        blank=False
    )
    profile_image = models.ImageField(
        verbose_name='프로필 사진',
        null=True
    )
    is_active = models.BooleanField(
        verbose_name='활성화 여부',
        null=False,
        default=True
    )

    department = models.ForeignKey(
        verbose_name='소속 학과',
        to=Department,
        on_delete=models.SET_NULL,
        null=True,
        related_name='department_user'
    )

    REQUIRED_FIELDS = ['email', 'studentId']
