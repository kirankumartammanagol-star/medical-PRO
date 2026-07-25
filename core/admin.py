from django.contrib import admin
from .models import UserProfile, Hospital, MedicalCollege, ContactMessage

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'specialization', 'experience_years')
    list_filter = ('role',)
    search_fields = ('user__username', 'user__first_name', 'specialization')

@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):
    list_display = ('name', 'hospital_type', 'city', 'beds_count', 'is_verified')
    list_filter = ('hospital_type', 'is_verified', 'state')
    search_fields = ('name', 'city')

@admin.register(MedicalCollege)
class MedicalCollegeAdmin(admin.ModelAdmin):
    list_display = ('name', 'university', 'city', 'total_students', 'placement_rate')
    search_fields = ('name', 'university')

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at', 'is_read')
    list_filter = ('is_read',)
