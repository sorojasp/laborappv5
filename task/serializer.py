from rest_framework import serializers
from task import models


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Task
        fields = ['id', 'description', 'fecha', 'porcentajeCumplimiento', 'tiempo', 'user']


class SubTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SubTask
        fields = ['id', 'description', 'porcentajeCumplimiento', 'task']


