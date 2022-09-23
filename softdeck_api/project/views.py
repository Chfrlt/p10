from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from .serializers import ProjectSerializer
from .models import Project
from contributors.models import Contributor
from softdeck_api.permissions import IsAuthor


class ProjectViewSet(ModelViewSet):
    """API endpoint for projects to be viewed or edited."""

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        IsAuthor,
    ]

    def get_queryset(self, *args, **kwargs):
        """
        Display a list of projects in which
        the user is either the author or a contributor.
        """
        contributors = Contributor.objects.filter(user_id=self.request.user.id)
        projects = [contributor.project.id for contributor in contributors]
        return Project.objects.filter(id__in=projects)

    def perform_create(self, serializer):
        serializer.save(author_user_id=self.request.user)

    def destroy(self, instance, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({
            "message":"Deleted successfully"
        },
        status=status.HTTP_200_OK)
