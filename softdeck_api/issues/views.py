from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from project.models import Project
from softdeck_api.permissions import IsProjectAuthor, IsContributor
from .models import Issue
from .serializers import IssueSerializer


class IssueViewSet(ModelViewSet):
    """API endpoint for issues to be viewed or edited."""

    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        IsProjectAuthor,
        IsContributor,
    ]

    def perform_create(self, serializer, **kwargs):
        """Create an issue for specified project."""
        project_pk = Project.objects.get(pk=self.kwargs["project_pk"])
        serializer.save(
            project_id=project_pk,
            author_user_id=self.request.user,
        )

    def get_queryset(self, **kwargs):
        """Display a list of issues for specified project."""
        return Issue.objects.filter(project_id=self.kwargs["project_pk"])
