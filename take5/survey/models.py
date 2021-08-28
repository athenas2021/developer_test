from django.contrib.auth.models import User
from django.db import models





class SurveyQuestion(models.Model):
    # survey  = models.ForeignKey(Survey, on_delete=models.CASCADE)
    questionText = models.CharField(max_length=255)
    questionAuthor = models.ForeignKey(User, on_delete=models.CASCADE)
    # questionAlternatives = models.ManyToOneRel(SurveyQuestionAlternative)
    # questionAlternatives = models.ManyToManyField(SurveyQuestionAlternative)
    # questionAlternatives = models.ForeignKey(SurveyQuestionAlternative, on_delete=models.CASCADE)
    def __str__(self):
        return self.questionText

class SurveyQuestionAlternative(models.Model):   
    question = models.ForeignKey(SurveyQuestion, on_delete=models.CASCADE)
    questionAlternativeText =  models.CharField(max_length=255)
    questionAlternative = models.CharField(max_length=1)
    rightAlternative = models.BooleanField()
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


# Create your models here.
