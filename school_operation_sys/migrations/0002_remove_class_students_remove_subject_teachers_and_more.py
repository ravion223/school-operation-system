# Generated by Django 5.0.2 on 2024-02-06 19:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_operation_sys', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='class',
            name='students',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='teachers',
        ),
        migrations.AddField(
            model_name='student',
            name='classes',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='school_operation_sys.class'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='school_operation_sys.subject'),
        ),
    ]
