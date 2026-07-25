from django.urls import path
from . import views

app_name = 'compliance'

urlpatterns = [
    path('', views.module_list, name='module_list'),
    path('module/<int:pk>/', views.training_module, name='training_module'),
    path('dashboard/', views.compliance_dashboard, name='compliance_dashboard'),
    path('certificate/<str:cert_id>/', views.download_certificate, name='certificate'),
]
