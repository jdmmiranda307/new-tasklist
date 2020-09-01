from .models import Task, Status
from rest_framework import serializers
from django.contrib.auth.models import User

class TaskSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)
    status = serializers.PrimaryKeyRelatedField(queryset=Status.objects.all(), required=False)

    class Meta:
        model = Task
        fields = ('id', 'user', 'title', 'status', 'description', 'created_at', 'updated_at', 'completed_at')

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'
