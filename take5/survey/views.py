from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.views.generic import DetailView, ListView
from survey.models import Survey, SurveyQuestion, SurveyQuestionAlternative 
from rest_framework import viewsets
from rest_framework import permissions
from survey.serializer import UserSerializer, SurveySerializer, SurveyQuestionSerializer, SurveyQuestionAlternativeSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    Rota para visualizar os usuários
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class SurveyQuestionViewSet(viewsets.ModelViewSet):
    """
    Rota para visualizar as questoes 
    """
    queryset = SurveyQuestion.objects.all()
    serializer_class = SurveyQuestionSerializer


class SurveyQuestionAlternativeViewSet(viewsets.ModelViewSet):
    """
    Rota para visualizar as alternativas das questoes 
    """
    queryset = SurveyQuestionAlternative.objects.all()
    serializer_class = SurveyQuestionAlternativeSerializer


class SurveyViewSet(viewsets.ModelViewSet):
    """
    Rota para visualizar pesquisas 
    """
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer


class SurveyListView(ListView):
    """
    Rota para view Html(/survey) visualizar pesquisas 
    """
    model: SurveyQuestion
    queryset = SurveyQuestion.objects.prefetch_related("survey")
    serializer_class = SurveyQuestionSerializer


class SurveyDetailView(DetailView):
    """
    To do:
    Rota para view Html(/survey/?) visualizar os detalhes da pesquisa
    """
    model: Survey