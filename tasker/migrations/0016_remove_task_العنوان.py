# Generated by Django 4.2 on 2023-04-13 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasker', '0015_delete_الوظيفة'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='العنوان',
        ),
    ]
