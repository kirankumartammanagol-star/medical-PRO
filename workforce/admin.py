from django.contrib import admin
from .models import WorkforceData, ForecastReport

@admin.register(WorkforceData)
class WorkforceDataAdmin(admin.ModelAdmin):
    list_display = ('specialty', 'region', 'demand', 'supply', 'year', 'quarter')
    list_filter = ('specialty', 'year', 'quarter')

@admin.register(ForecastReport)
class ForecastReportAdmin(admin.ModelAdmin):
    list_display = ('specialty', 'forecast_year', 'predicted_demand', 'predicted_shortage', 'shortage_level')
    list_filter = ('shortage_level', 'forecast_year')
