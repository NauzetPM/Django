# Generated by Django 5.1.2 on 2024-10-16 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_alter_task_description_alter_task_done_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='complete_before',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='done',
            field=models.BooleanField(default=False),
        ),
    ]
