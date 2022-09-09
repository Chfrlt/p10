"""
-un titre
-une description
-un type (back-end, front-end, iOS ou Android)
-un author_user_id.
"""
from django.conf import settings

from django.db import models


class Project(models.Model):
    PROJECT_TYPE_CHOICES = [
        ("front-end", "front-end"),
        ("back-end", "back-end"),
        ("iOS", "iOS"),
        ("Android", "Android"),
    ]

    title = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=50, choices=PROJECT_TYPE_CHOICES, default="front-end")
    author_user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'Project {self.id}: {self.title}'
