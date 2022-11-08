from django.db import models


class CoreModelNoID(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True
        ordering = ['-created_at', '-updated_at']

class CoreModel(CoreModelNoID):
    """Basic Model"""
    id = models.AutoField(primary_key=True, editable=False)


    class Meta:
        abstract = True
        ordering = ['-created_at', '-updated_at']
