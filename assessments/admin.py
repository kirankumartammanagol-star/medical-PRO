from django.contrib import admin
from .models import Assessment, Question, AssessmentResult, Certificate

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1

@admin.register(Assessment)
class AssessmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'difficulty', 'total_questions', 'passing_score', 'is_active')
    list_filter = ('category', 'difficulty', 'is_active')
    inlines = [QuestionInline]

@admin.register(AssessmentResult)
class AssessmentResultAdmin(admin.ModelAdmin):
    list_display = ('user', 'assessment', 'percentage', 'passed', 'completed_at')
    list_filter = ('passed', 'assessment')

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('user', 'assessment', 'issue_date', 'certificate_id')
    search_fields = ('certificate_id', 'user__username')
