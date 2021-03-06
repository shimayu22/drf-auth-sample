from rest_framework import generics
from rest_framework.permissions import DjangoModelPermissions
from .models import Todos
from .serializers import TodosSerializer

class TodoRead(generics.ListAPIView):
    """誰でも閲覧可能"""
    queryset = Todos.objects.all()
    serializer_class = TodosSerializer

class TodoCreate(generics.CreateAPIView):
    """add権限を持っているユーザーのみ、追加可能"""
    queryset = Todos.objects.all()
    serializer_class = TodosSerializer
    permission_classes = (DjangoModelPermissions,)

class TodoUpdate(generics.UpdateAPIView):
    """change権限を持っているユーザーのみ、編集可能"""
    queryset = Todos.objects.all()
    serializer_class = TodosSerializer
    permission_classes = (DjangoModelPermissions,)

class TodoDelete(generics.DestroyAPIView):
    """delete権限を持っているユーザーのみ、削除可能"""
    queryset = Todos.objects.all()
    serializer_class = TodosSerializer
    permission_classes = (DjangoModelPermissions,)

