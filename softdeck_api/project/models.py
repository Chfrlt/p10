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
    author_user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'Project id{self.id}: {self.title}'
