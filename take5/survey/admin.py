from django.contrib import admin

from .models import Survey, SurveyQuestion, SurveyQuestionAlternative

@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    list_display = ("surveyText",)

@admin.register(SurveyQuestion)
class SurveyQuestionAdmin(admin.ModelAdmin):
    list_display = ("questionText",)


@admin.register(SurveyQuestionAlternative)
class SurveyQuestionAlternativeAdmin(admin.ModelAdmin):
    list_display = ("questionAlternativeText",)

