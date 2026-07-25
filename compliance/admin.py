from django.contrib import admin
from .models import ComplianceModule, ComplianceQuiz, ComplianceRecord

class ComplianceQuizInline(admin.TabularInline):
    model = ComplianceQuiz
    extra = 1

@admin.register(ComplianceModule)
class ComplianceModuleAdmin(admin.ModelAdmin):
    list_display = ('title', 'regulation', 'required_score', 'is_mandatory')
    list_filter = ('regulation', 'is_mandatory')
    inlines = [ComplianceQuizInline]

@admin.register(ComplianceRecord)
class ComplianceRecordAdmin(admin.ModelAdmin):
    list_display = ('user', 'module', 'percentage', 'passed', 'completion_date')
    list_filter = ('passed', 'module')
