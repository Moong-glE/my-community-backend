from django.db import models

from mycomm.models.user import User
from mycomm.models.survey_question import SurveyQuestion


class SurveyAnswer(models.Model):
    answer = models.CharField(
        verbose_name='답변',
        max_length=300,
        null=False,
        blank=True
    )
    respondent = models.OneToOneField(
        verbose_name='답변자',
        to=User,
        on_delete=models.SET_NULL,
        null=False,
        related_name='respondent_answer'
    )
    question = models.ForeignKey(
        verbose_name='질문',
        to=SurveyQuestion,
        on_delete=models.CASCADE,
        null=False,
        related_name='question_answer'
    )
