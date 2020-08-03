from django.db import models
from django_file_validator.validators import MaxSizeValidator

from mycomm.models.article import Article


class ArticleFile(models.Model):
    # 1048576KB = 1GB
    FILE_SIZE_LIMIT_IN_KILOBYTES = 1048576
    file = models.FileField(
        verbose_name='첨부파일',
        validators=[MaxSizeValidator(FILE_SIZE_LIMIT_IN_KILOBYTES)],
        null=False,
        blank=False
    )
    article = models.ForeignKey(
        verbose_name='첨부파일의 게시물',
        to=Article,
        null=False,
        on_delete=models.CASCADE,
        related_name='article_articlefile'
    )
