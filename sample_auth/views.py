from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from .models import Todo
from .serializers import TodoSerializer

class TodoRead(generics.ListAPIView):
    """誰でも閲覧可能"""
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class TodoCreate(generics.CreateAPIView):
    """add権限を持っているユーザーのみ、追加可能"""
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated,)

class TodoUpdate(generics.UpdateAPIView):
    """change権限を持っているユーザーのみ、編集可能"""
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated,)

class TodoDelete(generics.DestroyAPIView):
    """管理者のみ、削除可能"""
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (IsAdminUser,)

