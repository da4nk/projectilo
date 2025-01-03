# Generated by Django 5.0.6 on 2024-05-27 07:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectillo', '0006_projects_owner'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='status',
            field=models.CharField(choices=[('NS', 'Not Started'), ('IP', 'In Progress'), ('C', 'Complete')], default=(('NS', 'Not Started'), ('IP', 'In Progress'), ('C', 'Complete')), max_length=3),
        ),
        migrations.AlterField(
            model_name='projects',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='owner', to=settings.AUTH_USER_MODEL),
        ),
    ]
