# Generated by Django 3.2.6 on 2021-08-28 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0005_auto_20210828_1131'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='surveyquestion',
            name='questionAlternatives',
        ),
        migrations.RemoveField(
            model_name='surveyuseranswer',
            name='questionAlternative',
        ),
        migrations.AddField(
            model_name='surveyquestionalternative',
            name='question',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='survey.surveyquestion'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='surveyuseranswer',
            name='questionQuestion',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='survey.surveyquestion'),
            preserve_default=False,
        ),
    ]
