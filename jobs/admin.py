from django.contrib import admin
from .models import JobListing, Application, Partnership

@admin.register(JobListing)
class JobListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'hospital_name', 'specialty', 'job_type', 'location', 'is_active', 'is_urgent')
    list_filter = ('specialty', 'job_type', 'is_active', 'is_urgent')
    search_fields = ('title', 'hospital_name', 'location')

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('candidate', 'job', 'status', 'applied_date')
    list_filter = ('status',)

@admin.register(Partnership)
class PartnershipAdmin(admin.ModelAdmin):
    list_display = ('hospital_name', 'college_name', 'program_type', 'students_enrolled', 'placement_rate', 'is_active')
    list_filter = ('program_type', 'is_active')
