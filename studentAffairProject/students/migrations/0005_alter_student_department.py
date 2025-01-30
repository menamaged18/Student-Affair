# Generated by Django 5.1.3 on 2024-12-15 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_alter_student_gpa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='department',
            field=models.CharField(blank=True, choices=[('ai', 'AI'), ('cs', 'CS'), ('it', 'IT'), ('is', 'IS'), ('ds', 'DS')], max_length=10, null=True),
        ),
    ]
