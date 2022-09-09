from django.db import models
from django.conf import settings
from issues.models import Issue

# Create your models here.
class Comment(models.Model):
    body = models.CharField(max_length=255)
    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        related_name='comments',
        on_delete=models.CASCADE,
        blank=True, null=True
        )
    issue_id = models.ForeignKey(
        Issue,
        related_name='comments',
        on_delete=models.CASCADE,
        blank=True,
        null=True
        )
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Issue : {self.issue_id.title}, Comment : {self.body}, Author : {self.author}"