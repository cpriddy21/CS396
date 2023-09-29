# Generated by Django 4.2.4 on 2023-09-24 21:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        #migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('OnlineLearningSystem', '0006_alter_practicequiz_question_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuizResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('chosen_choice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OnlineLearningSystem.choice')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OnlineLearningSystem.question')),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OnlineLearningSystem.practicequiz')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
