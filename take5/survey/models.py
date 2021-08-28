from django.contrib.auth.models import User
from django.db import models

class Survey(models.Model):
    title = models.CharField(max_length=255)

class SurveyQuestion(models.Model):
    survey  = models.ForeignKey(Survey, on_delete=models.CASCADE)
    question = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

class SurveyQuestionAlternative(models.Model):
    question= models.ForeignKey(SurveyQuestion, on_delete=models.CASCADE)
    questionAlternative = models.CharField(max_length=1)
    rightAlternative = models.BooleanField()

class SurveyUserAnswer(models.Model):
    questionAlternative = models.ForeignKey(SurveyQuestionAlternative, on_delete=models.CASCADE)
    userAnswer = models.CharField(max_length=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


# Create your models here.
