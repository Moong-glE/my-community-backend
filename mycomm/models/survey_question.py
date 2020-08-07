from django.db import models

from mycomm.models.survey import Survey


class SurveyQuestion(models.Model):
    question = models.CharField(
        verbose_name="질문내용",
        max_length=100,
        null=False,
        blank=False
    )
    survey = models.ForeignKey(
        verbose_name='설문',
        to=Survey,
        on_delete=models.CASCADE,
        null=False,
        related_name='survey_question'
    )
