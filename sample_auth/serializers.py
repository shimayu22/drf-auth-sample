from .models import Todo
from rest_framework import serializers

class TodoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Todo
    fields = ('id', 'memo', 'created_at', 'updated_at')