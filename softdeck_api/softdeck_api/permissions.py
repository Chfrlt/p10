from rest_framework import permissions

from contributors.models import Contributor
from project.models import Project

class IsProjectAuthor(permissions.BasePermission):
    """Custom permission, edition or deletion of an object is reserved to the author."""

    message = "Only possible if author"

    def has_object_permission(self, request, view, object):
        if request.method == "PUT" or request.method == "PATCH" or request.method == "DELETE":
            return request.user == object.author_user_id
        return True

class IsContributor(permissions.BasePermission):
    """Custom permission, allows the contributor of a project to view it."""

    message = "Only possible if contributor"

    def has_permission(self, request, view):
        project_pk = view.kwargs.get("project_pk")
        try:
            Contributor.objects.get(user_id=request.user.id, project=project_pk)
        except Contributor.DoesNotExist:
            return False
        return True
