# Generated by Django 4.1.2 on 2022-11-04 08:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_rename_inventory_user_inventory_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='inventory_id',
        ),
    ]
