# Generated by Django 3.2.9 on 2022-01-25 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0002_alter_player_auth_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='name',
            field=models.CharField(max_length=10, unique=True, verbose_name='name'),
        ),
    ]