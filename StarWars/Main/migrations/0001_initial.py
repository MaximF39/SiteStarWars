# Generated by Django 3.2.9 on 2022-01-25 12:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='name')),
                ('auth_key', models.CharField(max_length=32, verbose_name='auth_key')),
                ('race', models.IntegerField(choices=[(1, 'Омоленианин (Красные)'), (2, 'Иррииец (Жёлтые)'), (3, 'Анид (Зелёные)'), (4, 'Медрамилл (Синие)')], verbose_name='Race')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
    ]