# Generated by Django 3.2 on 2021-05-26 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cr', '0015_alter_task_rollback_point'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='eng_active',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
