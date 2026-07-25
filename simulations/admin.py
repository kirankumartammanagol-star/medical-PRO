from django.contrib import admin
from .models import Simulation, SimulationStep, SimulationAttempt

class SimulationStepInline(admin.TabularInline):
    model = SimulationStep
    extra = 1

@admin.register(Simulation)
class SimulationAdmin(admin.ModelAdmin):
    list_display = ('title', 'scenario_type', 'difficulty', 'is_active')
    list_filter = ('scenario_type', 'difficulty', 'is_active')
    inlines = [SimulationStepInline]

@admin.register(SimulationAttempt)
class SimulationAttemptAdmin(admin.ModelAdmin):
    list_display = ('user', 'simulation', 'percentage', 'completed_at')
