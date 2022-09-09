from rest_framework import viewsets, permissions
from rest_framework.response import Response
from django.shortcuts import render

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

    def create_contributor(self, serializer, **kwargs):
        """Add a contributor to a specific project."""
        project_pk = Project.objects.get(pk=self.kwargs["project_pk"])
        serializer.save(project=project_pk)

    def get_contributors(self, **kwargs):
        """Display the contributors of a project."""
        return Contributor.objects.filter(project=self.kwargs["project_pk"])

    def create(self, request, *args, **kwargs):
        """Add a contributor without specifying the project."""
        datas = request.data.copy()
        datas.__setitem__("project", self.kwargs["project_pk"])
        serializer = self.get_serializer(data=datas)
        serializer.is_valid(raise_exception=True)
        self.create_contributor(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, headers=headers)