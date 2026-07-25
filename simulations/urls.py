from django.urls import path
from . import views

app_name = 'simulations'

urlpatterns = [
    path('', views.simulation_list, name='simulation_list'),
    path('<int:pk>/', views.virtual_patient, name='virtual_patient'),
    path('results/', views.simulation_results, name='simulation_results'),
    path('certificate/<int:attempt_id>/', views.download_sim_certificate, name='certificate'),
]
