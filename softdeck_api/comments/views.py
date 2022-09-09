from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from issues.models import Issue
from softdeck_api.permissions import IsProjectAuthor, IsContributor
from .models import Comment
from .serializers import CommentSerializer


# Create your views here.
class CommentViewSet(ModelViewSet):
    """API endpoint for comments to be viewed or edited."""

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        IsProjectAuthor,
        IsContributor,
    ]

    def perform_create(self, serializer, **kwargs):
        """Create a comment for specified issue."""
        issue_pk = Issue.objects.get(pk=self.kwargs["issue_pk"])
        author_comment = self.request.user
        serializer.save(issue=issue_pk, author=author_comment)

    def get_queryset(self, **kwargs):
        """Display comments list for specified issue."""
        return Comment.objects.filter(issue=self.kwargs["issue_pk"])