from django.db import models
from django.conf import settings
from issues.models import Issue


class Comment(models.Model):
    description = models.CharField(max_length=255)
    author_user_id = models.ForeignKey(
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
        return (
            "Issue : {}, Comment : {}, Author : {}"
            .format(self.issue_id.title, self.description, self.author_user_id)
            )
