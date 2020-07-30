from django.db import models

from mycomm.models.user import User


class Article(models.Model):
    likeUsers = models.ManyToManyField(to=User, related_name="user_like_articles")
