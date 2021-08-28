from django.urls import path
from . import views

app_name = "survey"

urlpatterns = [
    path("",views.SurveyListView.as_view(), name="list"),
    #path("<questionAuthor:questionAuthor>/", views.SurveyDetailView.as_view(), name="detail"),
]

