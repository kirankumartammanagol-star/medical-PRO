from django.contrib import admin
from .models import Credential, VerificationRequest

@admin.register(Credential)
class CredentialAdmin(admin.ModelAdmin):
    list_display = ('user', 'credential_type', 'title', 'license_number', 'status', 'issue_date', 'expiry_date')
    list_filter = ('status', 'credential_type')
    search_fields = ('user__username', 'title', 'license_number')

@admin.register(VerificationRequest)
class VerificationRequestAdmin(admin.ModelAdmin):
    list_display = ('credential', 'requested_by', 'verification_status', 'created_at')
    list_filter = ('verification_status',)
