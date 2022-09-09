"""
-un titre
-une description
-un assigné (l’assigné par défaut étant l'auteur lui-même
-une priorité (FAIBLE, MOYENNE ou ÉLEVÉE)
-une balise (BUG, AMÉLIORATION ou TÂCHE) 
-un statut (À faire, En cours ou Terminé) 
-le project_id auquel il est lié et un created_time (horodatage)

ainsi que d'autres attributs mentionnés dans le diagramme de classe.
"""


from django.db import models
from django.conf import settings

from project.models import Project

# Create your models here.
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
    description = models.CharField(max_length=255, blank=True, null=True)
    priority = models.CharField(max_length=50, choices=PRIORITY_CHOICES, blank=True, null=True)
    tag = models.CharField(max_length=50, choices=TAG_CHOICES, blank=True, null=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, blank=True, null=True)
    project_id = models.ForeignKey(Project, related_name='issues', on_delete=models.CASCADE, blank=True, null=True)
    author = models.ForeignKey(
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
        return f'Project {self.project_id}: {self.project_id.title}, , Issue: {self.title}, Author: {self.author}:'
