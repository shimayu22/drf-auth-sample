from .models import Todos
from rest_framework import serializers

class TodosSerializer(serializers.ModelSerializer):
  class Meta:
    model = Todos
    fields = ('id', 'memo', 'created_at', 'updated_at')