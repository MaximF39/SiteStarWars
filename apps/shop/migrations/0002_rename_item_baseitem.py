# Generated by Django 4.1.2 on 2022-10-16 04:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Item',
            new_name='BaseItem',
        ),
    ]
