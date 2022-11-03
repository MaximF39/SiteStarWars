from django.db import models



class BaseModel(models.Model):
    """Basic Model"""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-created_at', '-updated_at']


class BaseModelID(BaseModel):
    """Basic Model"""
    id = models.AutoField(primary_key=True, editable=False)

    class Meta:
        abstract = True
        ordering = ['-created_at', '-updated_at']
