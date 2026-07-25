from django.urls import path
from . import views

app_name = 'workforce'

urlpatterns = [
    path('', views.demand_dashboard, name='demand_dashboard'),
    path('analysis/', views.specialty_analysis, name='specialty_analysis'),
]
