from django.contrib.auth.models import User
from rest_framework import serializers
from contributors.models import Contributor

from project.models import Project


class ContributorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contributor
        fields = '__all__'
