# Generated by Django 5.0.1 on 2025-03-12 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0002_rename_studentid_result_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default='2025-01-01 00:00:00'),
            preserve_default=False,
        ),
    ]
