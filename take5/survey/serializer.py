from django.contrib.auth.models import User, Group
from survey.models import Survey, SurveyQuestion, SurveyQuestionAlternative
from rest_framework import serializers
from rest_framework.validators import UniqueValidator   


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', ]


class SurveyQuestionAlternativeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurveyQuestionAlternative
        fields = ['question', 'questionAlternativeText','questionAlternative']


class SurveyQuestionSerializer(serializers.ModelSerializer):
    alternatives = SurveyQuestionAlternativeSerializer(many=True, read_only=True)
    class Meta:
        model = SurveyQuestion
        fields = ['questionText','survey','alternatives']

class SurveySerializer(serializers.ModelSerializer):   
    questions = SurveyQuestionSerializer(many=True, read_only=True) 
    class Meta:
        model = Survey
        fields = ('surveyText', 'surveyAuthor', 'questions')