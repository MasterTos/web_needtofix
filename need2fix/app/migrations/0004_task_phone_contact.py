# Generated by Django 2.0.6 on 2018-09-25 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_task_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='phone_contact',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
    ]
