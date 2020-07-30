from django.db import models

from mycomm.models.article import Article
from mycomm.models.department import Department


class User(models.Model):
    email = models.EmailField(verbose_name='이메일', null=False, unique=True)
    department = models.ForeignKey(verbose_name='소속 학과', to=Department, on_delete=models.CASCADE, null=False,
                                   related_name='department_user')
