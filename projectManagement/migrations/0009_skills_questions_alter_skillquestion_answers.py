# Generated by Django 4.1.6 on 2023-03-24 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectManagement', '0008_projectposition_skillquestion_skillquestionanswers_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='skills',
            name='questions',
            field=models.ManyToManyField(blank=True, related_name='question_skills_no', to='projectManagement.skillquestion', verbose_name='Вопросы'),
        ),
        migrations.AlterField(
            model_name='skillquestion',
            name='answers',
            field=models.ManyToManyField(blank=True, related_name='skill_question_answers_on', to='projectManagement.skillquestionanswers', verbose_name='Список ответов'),
        ),
    ]