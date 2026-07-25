from django.urls import path
from . import views

app_name = 'emr'

urlpatterns = [
    path('', views.emr_list, name='emr_list'),
    path('test/<int:pk>/', views.competency_test, name='competency_test'),
    path('certification/', views.certification, name='certification'),
    path('simulation/', views.simulation_dashboard, name='simulation'),
]
