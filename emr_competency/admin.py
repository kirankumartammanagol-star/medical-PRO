from django.contrib import admin
from .models import EMRSystem, CompetencyTest, CompetencyQuestion, CompetencyResult

@admin.register(EMRSystem)
class EMRSystemAdmin(admin.ModelAdmin):
    list_display = ('name', 'vendor', 'version', 'is_active')

class CompetencyQuestionInline(admin.TabularInline):
    model = CompetencyQuestion
    extra = 1

@admin.register(CompetencyTest)
class CompetencyTestAdmin(admin.ModelAdmin):
    list_display = ('title', 'standard', 'passing_score', 'is_active')
    inlines = [CompetencyQuestionInline]

@admin.register(CompetencyResult)
class CompetencyResultAdmin(admin.ModelAdmin):
    list_display = ('user', 'test', 'percentage', 'certified', 'certificate_number')
