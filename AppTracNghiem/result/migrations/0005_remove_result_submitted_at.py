# Generated by Django 5.0.1 on 2025-03-12 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0004_result_total_questions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result',
            name='submitted_at',
        ),
    ]
