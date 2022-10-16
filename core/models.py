from django.db import models


class BaseModel(models.Model):
    """Basic Model"""
    id = models.AutoField(primary_key=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    properties = models.JSONField(null=True)

    class Meta:
        abstract = True
        ordering = ['-created_at', '-updated_at']
