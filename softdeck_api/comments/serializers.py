from rest_framework import serializers

from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author_user_id.username")
    issue = serializers.ReadOnlyField(source="issue.title")

    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ["author_user_id", "issue"]
