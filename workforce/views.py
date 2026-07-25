from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import WorkforceData, ForecastReport
from django.db.models import Sum, Avg


@login_required
def demand_dashboard(request):
    """Workforce demand analysis dashboard"""
    workforce_data = WorkforceData.objects.all()
    forecasts = ForecastReport.objects.all()

    # Aggregate by specialty
    specialty_stats = []
    for code, name in WorkforceData.SPECIALTY_CHOICES:
        data = workforce_data.filter(specialty=code)
        if data.exists():
            total_demand = data.aggregate(Sum('demand'))['demand__sum'] or 0
            total_supply = data.aggregate(Sum('supply'))['supply__sum'] or 0
            avg_salary = data.aggregate(Avg('avg_salary'))['avg_salary__avg'] or 0
            shortage = max(total_demand - total_supply, 0)
            ratio = total_supply / max(total_demand, 1)
            if ratio >= 0.9:
                level = 'Low'
                color = '#43e97b'
            elif ratio >= 0.7:
                level = 'Moderate'
                color = '#f9d423'
            elif ratio >= 0.5:
                level = 'High'
                color = '#fa709a'
            else:
                level = 'Critical'
                color = '#ff416c'

            specialty_stats.append({
                'name': name,
                'code': code,
                'demand': total_demand,
                'supply': total_supply,
                'shortage': shortage,
                'level': level,
                'color': color,
                'avg_salary': round(avg_salary, 2),
            })

    # If no data, show sample data
    if not specialty_stats:
        specialty_stats = [
            {'name': 'General Medicine', 'demand': 15000, 'supply': 12000, 'shortage': 3000, 'level': 'Moderate', 'color': '#f9d423', 'avg_salary': 120000},
            {'name': 'Surgery', 'demand': 8000, 'supply': 5500, 'shortage': 2500, 'level': 'High', 'color': '#fa709a', 'avg_salary': 250000},
            {'name': 'Pediatrics', 'demand': 10000, 'supply': 9200, 'shortage': 800, 'level': 'Low', 'color': '#43e97b', 'avg_salary': 110000},
            {'name': 'Cardiology', 'demand': 5000, 'supply': 3000, 'shortage': 2000, 'level': 'High', 'color': '#fa709a', 'avg_salary': 300000},
            {'name': 'Neurology', 'demand': 4000, 'supply': 2200, 'shortage': 1800, 'level': 'High', 'color': '#fa709a', 'avg_salary': 280000},
            {'name': 'Oncology', 'demand': 3500, 'supply': 2000, 'shortage': 1500, 'level': 'Critical', 'color': '#ff416c', 'avg_salary': 320000},
            {'name': 'Emergency Medicine', 'demand': 12000, 'supply': 8000, 'shortage': 4000, 'level': 'High', 'color': '#fa709a', 'avg_salary': 150000},
            {'name': 'Nursing', 'demand': 50000, 'supply': 35000, 'shortage': 15000, 'level': 'High', 'color': '#fa709a', 'avg_salary': 45000},
            {'name': 'Radiology', 'demand': 6000, 'supply': 5000, 'shortage': 1000, 'level': 'Moderate', 'color': '#f9d423', 'avg_salary': 200000},
            {'name': 'Pharmacy', 'demand': 20000, 'supply': 18000, 'shortage': 2000, 'level': 'Low', 'color': '#43e97b', 'avg_salary': 55000},
        ]

    stats = {
        'total_demand': sum(s['demand'] for s in specialty_stats),
        'total_supply': sum(s['supply'] for s in specialty_stats),
        'total_shortage': sum(s['shortage'] for s in specialty_stats),
        'critical_count': sum(1 for s in specialty_stats if s['level'] in ['Critical', 'High']),
    }

    return render(request, 'workforce/demand_dashboard.html', {
        'specialty_stats': specialty_stats,
        'forecasts': forecasts[:10],
        'stats': stats,
    })


@login_required
def specialty_analysis(request):
    """Detailed specialty analysis"""
    specialty = request.GET.get('specialty', 'general_medicine')
    data = WorkforceData.objects.filter(specialty=specialty)

    # Sample trend data for visualization
    trend_data = {
        'labels': ['2022 Q1', '2022 Q2', '2022 Q3', '2022 Q4', '2023 Q1', '2023 Q2', '2023 Q3', '2023 Q4', '2024 Q1', '2024 Q2', '2024 Q3', '2024 Q4', '2025 Q1', '2025 Q2', '2025 Q3', '2025 Q4', '2026 Q1'],
        'demand': [10000, 10500, 11000, 11500, 12000, 12500, 13000, 13500, 14000, 14500, 15000, 15500, 16000, 16500, 17000, 17500, 18000],
        'supply': [9000, 9200, 9400, 9600, 9800, 10000, 10200, 10400, 10600, 10800, 11000, 11200, 11400, 11600, 11800, 12000, 12200],
    }

    regions = [
        {'name': 'North India', 'demand': 4500, 'supply': 3200, 'shortage': 1300},
        {'name': 'South India', 'demand': 5000, 'supply': 4200, 'shortage': 800},
        {'name': 'East India', 'demand': 3000, 'supply': 1800, 'shortage': 1200},
        {'name': 'West India', 'demand': 4000, 'supply': 3500, 'shortage': 500},
        {'name': 'Central India', 'demand': 2500, 'supply': 1500, 'shortage': 1000},
    ]

    specialties = WorkforceData.SPECIALTY_CHOICES

    return render(request, 'workforce/specialty_analysis.html', {
        'data': data,
        'trend_data': trend_data,
        'regions': regions,
        'selected_specialty': specialty,
        'specialties': specialties,
    })
