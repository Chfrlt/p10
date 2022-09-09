from django.conf import settings
from django.db import models
from project.models import Project


class Contributor(models.Model):
    username = models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='contributors',
                                on_delete=models.CASCADE, blank=True, null=True)
    project = models.ForeignKey(Project, related_name='contributors',
                                on_delete=models.CASCADE, blank=True, null=True)
    permission = models.CharField(max_length=11, blank=True, null=True)
    role = models.CharField(max_length=128, blank=True, null=True)