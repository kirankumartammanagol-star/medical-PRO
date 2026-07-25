"""
URL configuration for healthcare_portal project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('credentials/', include('credentials.urls')),
    path('assessments/', include('assessments.urls')),
    path('emr/', include('emr_competency.urls')),
    path('compliance/', include('compliance.urls')),
    path('simulations/', include('simulations.urls')),
    path('workforce/', include('workforce.urls')),
    path('jobs/', include('jobs.urls')),
    path('api/v1/', include('core.api_urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
