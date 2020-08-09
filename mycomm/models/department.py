from django.db import models

class Department(models.Model):
    name = models.CharField(
        verbose_name='학과 이름',
        max_length=255,
        null=False,
        blank=False
    )
    university = models.CharField(
        verbose_name='학교 이름',
        max_length=100,
        null=False,
        blank=False
    )

    class Meta:
        unique_together = ('name', 'university')
