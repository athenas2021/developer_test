from django.contrib.auth.models import User
from django.db import models

class Survey(models.Model):
    """
    Model: Pesquisa
    """    
    surveyText = models.CharField(max_length=255)
    surveyAuthor = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):              
        return  self.surveyText


class SurveyQuestion(models.Model):
    """
    Model: Questao
    """
    survey =  models.ForeignKey(Survey, on_delete=models.CASCADE)
    questionText = models.CharField(max_length=255)        
    def __str__(self):
        return self.questionText


class SurveyQuestionAlternative(models.Model):
    """
    Model: Alternativa
    """   
    question = models.ForeignKey(SurveyQuestion, on_delete=models.CASCADE)
    questionAlternativeText =  models.CharField(max_length=255)
    questionAlternative = models.CharField(max_length=1)
    def __str__(self):
        return self.questionAlternativeText
   

class SurveyUserAnswer(models.Model):
    """
    Model: Resposta
    """
    question = models.ForeignKey(SurveyQuestion, on_delete=models.CASCADE)
    userAnswer = models.CharField(max_length=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.userAnswer
