from rest_framework.response import Response
from rest_framework.permissions import BasePermission
from .models import Task, Status
from .serializers import TaskSerializer, StatusSerializer
from rest_framework import viewsets, status
from rest_framework.decorators import action, permission_classes
from django.utils import timezone
from django.shortcuts import get_object_or_404


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user:
            return obj.user == request.user
        return False


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = (IsOwner,)

    def get_queryset(self):
        user = self.request.user
        queryset = Task.objects.all().filter(user=user).order_by('-created_at')
        queryset = Task.objects.all().order_by('-created_at')
        return queryset

    def create(self, request):
        data = request.data
        data['user'] = request.user.id
        data['status'] = 1
        serializer = TaskSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
