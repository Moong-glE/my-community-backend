from django.db import models

from mycomm.models.department import Department
from mycomm.models.user import User


class DeptApply(models.Model):
    replied_at = models.DateTimeField(
        verbose_name='응답 일시',
        null=True,
        blank=False
    )

    is_accepted = models.BooleanField(
        verbose_name='수락 여부',
        null=False,
        default=False
    )

    rejected_message = models.CharField(
        verbose_name='거절 메세지',
        max_length=255,
        null=True,
        blank=False
    )

    reviewer = models.ForeignKey(
        verbose_name='리뷰어',
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='reviewer_dept_apply'
    )

    department = models.ForeignKey(
        verbose_name="학과",
        to=Department,
        on_delete=models.CASCADE,
        null=False,
        related_name='department_dept_apply'
    )

    applier = models.ForeignKey(
        verbose_name='신청 유저',
        to=User,
        on_delete=models.SET_NULL,
        null=False,
        related_name='user_dept_apply'
    )
