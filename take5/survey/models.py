from django.contrib.auth.models import User
from django.db import models

class SurveyQuestion(models.Model):
    questionText = models.CharField(max_length=255)
    questionAuthor = models.ForeignKey(User, on_delete=models.CASCADE)    
    def __str__(self):
        return self.questionText

class SurveyQuestionAlternative(models.Model):   
    question = models.ForeignKey(SurveyQuestion, on_delete=models.CASCADE)
    questionAlternativeText =  models.CharField(max_length=255)
    questionAlternative = models.CharField(max_length=1)
    def __str__(self):
        return self.questionAlternativeText

class Survey(models.Model):
    surveyText = models.CharField(max_length=255)
    surveyQuestions = models.ManyToManyField(SurveyQuestion)
    def __str__(self):
        return self.surveyText    

class SurveyUserAnswer(models.Model):
    questionQuestion = models.ForeignKey(SurveyQuestion, on_delete=models.CASCADE)
    userAnswer = models.CharField(max_length=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.userAnswer
