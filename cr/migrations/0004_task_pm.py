# Generated by Django 3.2 on 2021-05-06 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cr', '0003_alter_engineer_eng_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='pm',
            field=models.CharField(default='test user', max_length=50),
            preserve_default=False,
        ),
    ]