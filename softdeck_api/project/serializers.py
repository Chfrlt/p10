from rest_framework import serializers
from .models import Project
from contributors.models import Contributor

class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = "__all__"
        read_only_fields = ["author"]
    
    def create(self, validated_data):
        """
        Create a new project,
        The creator is also the first contributor.
        """
        new_project = Project.objects.create(**validated_data)
        new_project.author_user_id = self.context["request"].user.id
        new_project.save()
        Contributor.objects.create(
            user=self.context["request"].user,
            project=new_project,
            role="Team leader"
        )
        return