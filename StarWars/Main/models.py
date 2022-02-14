import hmac
import uuid

from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Player(models.Model):
    auth_key = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(verbose_name='name', unique=True, max_length=10)
    # auth_key = models.UUIDField(verbose_name='auth_key')
    # auth_key = models.CharField(verbose_name='auth_key', unique=True, max_length=32, default=auth)
    race_type = (
        (1, 'Омоленианин (Красные)'),
        (2, 'Иррииец (Жёлтые)'),
        (3, 'Анид (Зелёные)'),
        (4, 'Медрамилл (Синие)'),
    )
    race = models.IntegerField(verbose_name='Race', choices=race_type)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
