from rest_framework import viewsets, permissions
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status

from .models import Contributor
from .serializers import ContributorSerializer
from project.models import Project
from softdeck_api.permissions import IsContributor


class ContributorViewSet(viewsets.ModelViewSet):

    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        IsContributor,
    ]

    def perform_create(self, serializer, **kwargs):
        """Add a contributor to a specified project."""
        user_id = User.objects.get(username=self.request.POST['user'])
        project_pk = Project.objects.get(pk=self.kwargs["project_pk"])
        serializer.save(project=project_pk, user_id=user_id)

    def get_contributors(self, **kwargs):
        """Display the contributors of a project."""
        return Contributor.objects.filter(project=self.kwargs["project_pk"])

    def destroy(self, instance, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message":"Deleted successfully"},
                        status=status.HTTP_200_OK)
