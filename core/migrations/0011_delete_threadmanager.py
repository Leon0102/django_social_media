# Generated by Django 4.0.4 on 2022-06-04 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_threadmanager'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ThreadManager',
        ),
    ]