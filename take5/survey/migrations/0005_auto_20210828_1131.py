# Generated by Django 3.2.6 on 2021-08-28 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0004_auto_20210828_1126'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='surveyquestion',
            name='survey',
        ),
        migrations.AddField(
            model_name='survey',
            name='surveyQuestions',
            field=models.ManyToManyField(to='survey.SurveyQuestion'),
        ),
    ]
