from django.contrib.auth.models import User
from django.views.generic import DetailView, ListView
from survey.models import Survey, SurveyQuestion, SurveyQuestionAlternative
from rest_framework import viewsets
from rest_framework import permissions
from survey.serializer import UserSerializer, SurveySerializer, SurveyQuestionSerializer, SurveyQuestionAlternativeSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]



class SurveyQuestionViewSet(viewsets.ModelViewSet):
    queryset = SurveyQuestion.objects.all()
    serializer_class = SurveyQuestionSerializer

class SurveyQuestionAlternativeViewSet(viewsets.ModelViewSet):
    queryset = SurveyQuestionAlternative.objects.all()
    serializer_class = SurveyQuestionAlternativeSerializer

class SurveyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows surveys to be viewed or edited.
    """
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer
    # permission_classes = [permissions.IsAuthenticated]

class SurveyListView(ListView):
    model: Survey
    queryset = Survey.objects.all()


class SurveyDetailView(DetailView):
    model: Survey