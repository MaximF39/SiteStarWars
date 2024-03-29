# Generated by Django 4.1.2 on 2022-11-04 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_remove_user_inventory_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
