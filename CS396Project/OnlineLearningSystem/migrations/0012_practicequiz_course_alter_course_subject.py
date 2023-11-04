# Generated by Django 4.2.4 on 2023-11-03 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('OnlineLearningSystem', '0011_course_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='practicequiz',
            name='course',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='quizzes', to='OnlineLearningSystem.course'),
        ),
        migrations.AlterField(
            model_name='course',
            name='subject',
            field=models.CharField(blank=True, default=None, max_length=35, null=True),
        ),
    ]
