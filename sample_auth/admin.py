from django.contrib import admin
from django.db import models
from .models import Todos

# Register your models here.
class TodosAdmin(admin.ModelAdmin):
    list_display = (
      'id',
      'memo',
      'created_at',
      'updated_at'
    )

admin.site.register(Todos,TodosAdmin)
