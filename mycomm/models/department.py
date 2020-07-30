from django.db import models


class Department(models.Model):
    name = models.CharField(verbose_name="이름", max_length=100, null=False)
    university = models.CharField(verbose_name="대학교", max_length=100)
    secret_value = models.CharField(verbose_name="밝혀지면 앙대", max_length=50)
