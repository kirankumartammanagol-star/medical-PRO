from django.urls import path
from . import api_views

app_name = 'api'

urlpatterns = [
    path('auth/login/', api_views.api_login, name='api_login'),
    path('profile/', api_views.api_profile, name='api_profile'),
    path('jobs/', api_views.api_jobs, name='api_jobs'),
    path('credentials/', api_views.api_credentials, name='api_credentials'),
    path('assessments/', api_views.api_assessments, name='api_assessments'),
    path('emr_tests/', api_views.api_emr_tests, name='api_emr_tests'),
    path('compliance/', api_views.api_compliance, name='api_compliance'),
    path('simulations/', api_views.api_simulations, name='api_simulations'),
]
