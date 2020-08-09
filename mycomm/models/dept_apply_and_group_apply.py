from django.db import models

from mycomm.models.user import User


class DeptApplyAndGroupApply(models.Model):
    replied_at = models.DateTimeField(
        verbose_name='응답 시간',
        null=False,
        blank=False
    )

    is_accepted = models.BooleanField(
        verbose_name='허용 여부',
        null=False,
        default=False
    )

    rejected_message = models.CharField(
        verbose_name='거절 메세지',
        max_length=255,
        null=False,
        blank=False
    )

    reviewer = models.ForeignKey(
        verbose_name='리뷰어',
        to=User,
        on_delete=models.CASCADE,
        null=False,
        related_name='reviewer_apply'
    )

    # Or는 뭐지

    user = models.ForeignKey(
        verbose_name='사용자 명단',
        to=User,
        on_delete=models.CASCADE,
        null=False,
        related_name='user_apply'
    )
