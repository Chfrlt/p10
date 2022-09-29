from django.db import models
from django.conf import settings

from project.models import Project


class Issue(models.Model):

    PRIORITY_CHOICES = [
        ("Low", "Low"),
        ("Middle", "Middle"),
        ("High", "High"),
    ]
    TAG_CHOICES = [
        ("Bug", "Bug"),
        ("Improve", "Improve"),
        ("Task", "Task"),
    ]
    STATUS_CHOICES = [
        ("To do", "To do"),
        ("Ongoing", "Ongoing"),
        ("Completed", "Completed"),
    ]

    title = models.CharField(max_length=255)
    description = models.CharField(
        max_length=255, blank=True, null=True)
    priority = models.CharField(
        max_length=50, choices=PRIORITY_CHOICES, blank=True, null=True)
    tag = models.CharField(
        max_length=50, choices=TAG_CHOICES, blank=True, null=True)
    status = models.CharField(
        max_length=50, choices=STATUS_CHOICES, blank=True, null=True)
    project_id = models.ForeignKey(
        Project, related_name='issues',
        on_delete=models.CASCADE, blank=True, null=True)
    author_user_id = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="author",
        blank=True,
        null=True,
        )
    assignee_user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="assignee_user",
        blank=True,
        null=True
        )
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            '{}, Issue: {}, Author: {}:'
            .format(self.project_id, self.title, self.author_user_id))
