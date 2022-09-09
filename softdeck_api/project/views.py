from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from .serializers import ProjectSerializer
from .models import Project
from contributors.models import Contributor
from softdeck_api.permissions import IsProjectAuthor
# Create your views here.


class ProjectViewSet(ModelViewSet):
    """API endpoint for projects to be viewed or edited."""

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        IsProjectAuthor,
    ]

    def get_queryset(self, *args, **kwargs):
        """
        Display a list of projects in which
        the user is either the author or a contributor.
        """
        contributors = Contributor.objects.filter(username=self.request.user)
        projects = [contributor.project.id for contributor in contributors]
        return Project.objects.filter(id__in=projects)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
