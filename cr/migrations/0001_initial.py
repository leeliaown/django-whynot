# Generated by Django 3.2 on 2021-05-06 08:45

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Engineer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('eng_id', models.CharField(max_length=50)),
                ('created_date', models.DateField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cr_date', models.DateField()),
                ('project_name', models.CharField(blank=True, max_length=200)),
                ('cr_description', models.CharField(max_length=100)),
                ('cr_project_code', models.CharField(max_length=100)),
                ('attendance_point', models.SmallIntegerField(choices=[(0, 'Failed'), (1, 'Okay')])),
                ('result_point', models.SmallIntegerField(choices=[(0, 'Failed'), (1, 'Okay')])),
                ('pm', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cr.engineer')),
            ],
        ),
    ]
