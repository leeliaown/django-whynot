# Generated by Django 3.2 on 2021-05-10 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cr', '0008_alter_task_remark'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='remark',
            field=models.CharField(blank=True, default='test', max_length=100),
            preserve_default=False,
        ),
    ]