# Create your models here.
from django.db import models
from django.core import serializers


class MLModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.EmailField()
    name = models.TextField()
    artifact_location = models.TextField()
    account_id = models.BigIntegerField()
    qbol_user_id = models.BigIntegerField()

    class Meta:
        ordering = ('created_at',)


class ModelParam(models.Model):
    key = models.TextField()
    value = models.TextField()
    model = models.ForeignKey(MLModel, related_name="model_params", blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return serializers.serialize("json", ModelParam.objects.all())

