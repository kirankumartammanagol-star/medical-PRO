from django.urls import path
from . import views

app_name = 'credentials'

urlpatterns = [
    path('', views.credential_list, name='credential_list'),
    path('submit/', views.credential_submit, name='credential_submit'),
    path('verification/', views.verification_dashboard, name='verification_dashboard'),
    path('<int:pk>/', views.credential_detail, name='credential_detail'),
]
