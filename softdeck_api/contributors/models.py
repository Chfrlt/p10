from django.conf import settings
from django.db import models
from project.models import Project


class Contributor(models.Model):
    user_id = models.IntegerField(verbose_name='contributors', blank=True, null=False)
    project = models.ForeignKey(Project, related_name='contributors',
                                on_delete=models.CASCADE, blank=True, null=True)
    role = models.CharField(max_length=128, blank=True, null=False)
