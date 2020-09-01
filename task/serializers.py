from .models import Task, Status
from rest_framework import serializers
from django.contrib.auth.models import User


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)
    status = serializers.PrimaryKeyRelatedField(queryset=Status.objects.all(), required=False)

    class Meta:
        model = Task
        fields = ('id', 'user', 'title', 'status', 'description', 'created_at', 'updated_at', 'completed_at')

    def to_representation(self, value):
        data = super().to_representation(value)
        data['status'] = StatusSerializer(Status.objects.get(id=data['status'])).data
        return data
