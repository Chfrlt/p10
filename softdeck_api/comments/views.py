from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from issues.models import Issue
from softdeck_api.permissions import IsAuthor, IsContributor
from .models import Comment
from .serializers import CommentSerializer


class CommentViewSet(ModelViewSet):
    """API endpoint for comments to be viewed or edited."""

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        IsAuthor,
        IsContributor,
    ]

    def perform_create(self, serializer, **kwargs):
        """Create a comment for specified issue."""
        issue = Issue.objects.get(pk=self.kwargs["issues_pk"])
        comment_author = self.request.user
        serializer.save(issue_id=issue, author_user_id=comment_author)

    def get_queryset(self, **kwargs):
        """Display comments list for specified issue."""
        return Comment.objects.filter(issue_id=self.kwargs["issues_pk"])

    def destroy(self, instance, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message":"Deleted successfully"},
                        status=status.HTTP_200_OK)
