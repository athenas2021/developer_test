from django.contrib.auth.models import User, Group
from survey.models import Survey, SurveyQuestion, SurveyQuestionAlternative
from rest_framework import serializers
from rest_framework.validators import UniqueValidator   


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class SurveyQuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SurveyQuestion
        fields = ['questionText', 'questionAuthor']

class SurveyQuestionAlternativeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SurveyQuestionAlternative
        fields = ['question', 'questionAlternativeText','questionAlternative']


class SurveySerializer(serializers.HyperlinkedModelSerializer):    
    class Meta:
        model = Survey
        fields = ('surveyText', 'surveyQuestions')