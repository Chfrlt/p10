from rest_framework import serializers
from .models import Issue

class IssueSerializer(serializers.ModelSerializer):

    class Meta:
        model = Issue
        fields = "__all__"

    def create(self, validated_data):
        new_issue = Issue.objects.create(**validated_data)
        new_issue.assignee_user = self.context["request"].user.id
        new_issue.author_user_id = self.context["request"].user.id
        new_issue.save()
        return