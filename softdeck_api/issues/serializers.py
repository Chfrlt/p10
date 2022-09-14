from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Issue

class IssueSerializer(serializers.ModelSerializer):

    assignee_user = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        many=False,
        read_only=False,
        slug_field='username'
    )


    class Meta:
        model = Issue
        fields = "__all__"

    def create(self, validated_data):
        new_issue = Issue.objects.create(**validated_data)
        new_issue.author_user_id = self.context["request"].user
        new_issue.save()
        return new_issue
