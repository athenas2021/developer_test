from django.urls import path
from . import views

app_name = "survey"

urlpatterns = [
    path("",views.SurveyListView.as_view(), name="list"),
    #path("<surveyAuthor:surveyAuthor>/", views.SurveyDetailView.as_view(), name="detail"),
]

