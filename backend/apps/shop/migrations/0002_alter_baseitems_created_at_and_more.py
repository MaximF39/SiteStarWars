# Generated by Django 4.1.2 on 2022-11-04 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseitems',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='baseitems',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
