from django.db import models

# Create your models here.

class Todos(models.Model):
    memo = models.CharField(
      verbose_name="TODO",
      max_length=50,
    )

    created_at = models.DateTimeField(
      verbose_name="登録日",
      auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        verbose_name="更新日",
        auto_now=True,
    )

    class Meta:
      verbose_name = "TODO"
      verbose_name_plural = "TODO"

