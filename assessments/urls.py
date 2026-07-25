from django.urls import path
from . import views

app_name = 'assessments'

urlpatterns = [
    path('', views.assessment_list, name='assessment_list'),
    path('take/<int:pk>/', views.take_assessment, name='take_assessment'),
    path('results/', views.assessment_results, name='results'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('certificate/<int:pk>/', views.download_certificate, name='certificate'),
]
