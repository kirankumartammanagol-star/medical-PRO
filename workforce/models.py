from django.db import models


class WorkforceData(models.Model):
    SPECIALTY_CHOICES = [
        ('general_medicine', 'General Medicine'),
        ('surgery', 'Surgery'),
        ('pediatrics', 'Pediatrics'),
        ('cardiology', 'Cardiology'),
        ('neurology', 'Neurology'),
        ('oncology', 'Oncology'),
        ('orthopedics', 'Orthopedics'),
        ('radiology', 'Radiology'),
        ('anesthesiology', 'Anesthesiology'),
        ('emergency_medicine', 'Emergency Medicine'),
        ('psychiatry', 'Psychiatry'),
        ('dermatology', 'Dermatology'),
        ('ophthalmology', 'Ophthalmology'),
        ('nursing', 'Nursing'),
        ('pharmacy', 'Pharmacy'),
        ('lab_technician', 'Lab Technician'),
        ('physical_therapy', 'Physical Therapy'),
        ('respiratory_therapy', 'Respiratory Therapy'),
        ('medical_assisting', 'Medical Assisting'),
        ('healthcare_it', 'Healthcare IT'),
    ]

    specialty = models.CharField(max_length=30, choices=SPECIALTY_CHOICES)
    region = models.CharField(max_length=100)
    demand = models.IntegerField(default=0, help_text="Number of positions needed")
    supply = models.IntegerField(default=0, help_text="Number of qualified professionals available")
    year = models.IntegerField(default=2026)
    quarter = models.CharField(max_length=2, choices=[('Q1','Q1'),('Q2','Q2'),('Q3','Q3'),('Q4','Q4')])
    avg_salary = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    growth_rate = models.FloatField(default=0, help_text="Percentage growth")
    
    # Enhanced workforce data fields
    population_served = models.IntegerField(default=0, help_text="Population served in region")
    healthcare_facilities = models.IntegerField(default=0, help_text="Number of healthcare facilities")
    aging_population_percentage = models.FloatField(default=0, help_text="Percentage of population over 65")
    chronic_disease_prevalence = models.FloatField(default=0, help_text="Prevalence of chronic diseases")
    telehealth_adoption = models.FloatField(default=0, help_text="Telehealth adoption rate")
    retirement_rate = models.FloatField(default=0, help_text="Annual retirement rate")
    turnover_rate = models.FloatField(default=0, help_text="Annual turnover rate")
    training_capacity = models.IntegerField(default=0, help_text="Annual training capacity")
    immigration_impact = models.FloatField(default=0, help_text="Impact of immigration on workforce")
    technology_automation = models.FloatField(default=0, help_text="Impact of technology/automation")
    policy_changes = models.TextField(blank=True, help_text="Relevant policy changes affecting demand")
    economic_factors = models.TextField(blank=True, help_text="Economic factors affecting workforce")
    pandemic_impact = models.FloatField(default=0, help_text="COVID-19 pandemic impact score")
    seasonal_variations = models.JSONField(default=dict, blank=True, help_text="Seasonal demand variations")
    demographic_trends = models.JSONField(default=dict, blank=True, help_text="Demographic trend data")

    @property
    def shortage(self):
        return max(self.demand - self.supply, 0)

    @property
    def shortage_level(self):
        ratio = self.supply / max(self.demand, 1)
        if ratio >= 0.9:
            return 'Low'
        elif ratio >= 0.7:
            return 'Moderate'
        elif ratio >= 0.5:
            return 'High'
        return 'Critical'

    def __str__(self):
        return f"{self.get_specialty_display()} - {self.region} ({self.year} {self.quarter})"

    class Meta:
        ordering = ['year', 'quarter', 'specialty']
        verbose_name_plural = 'Workforce Data'


class ForecastReport(models.Model):
    specialty = models.CharField(max_length=30, choices=WorkforceData.SPECIALTY_CHOICES)
    region = models.CharField(max_length=100, default='All India')
    predicted_demand = models.IntegerField(default=0)
    predicted_supply = models.IntegerField(default=0)
    predicted_shortage = models.IntegerField(default=0)
    shortage_level = models.CharField(max_length=20, default='Low')
    forecast_year = models.IntegerField(default=2027)
    confidence_score = models.FloatField(default=0.85)
    recommendations = models.TextField(blank=True)
    generated_date = models.DateTimeField(auto_now_add=True)
    
    # Enhanced forecast report fields
    forecast_methodology = models.CharField(max_length=100, choices=[
        ('linear_regression', 'Linear Regression'),
        ('time_series', 'Time Series Analysis'),
        ('machine_learning', 'Machine Learning'),
        ('hybrid', 'Hybrid Model'),
        ('expert_opinion', 'Expert Opinion'),
    ], default='machine_learning')
    data_sources = models.JSONField(default=list, blank=True, help_text="Data sources used for forecasting")
    key_drivers = models.JSONField(default=dict, blank=True, help_text="Key factors driving the forecast")
    risk_factors = models.JSONField(default=list, blank=True, help_text="Risk factors affecting accuracy")
    scenario_analysis = models.JSONField(default=dict, blank=True, help_text="Best/worst case scenarios")
    intervention_impact = models.JSONField(default=dict, blank=True, help_text="Impact of potential interventions")
    market_trends = models.TextField(blank=True, help_text="Relevant market trends")
    technological_disruptions = models.TextField(blank=True, help_text="Potential technological disruptions")
    policy_impact_assessment = models.TextField(blank=True, help_text="Impact of healthcare policies")
    economic_outlook = models.TextField(blank=True, help_text="Economic factors affecting forecast")
    competitive_landscape = models.TextField(blank=True, help_text="Competitive analysis")
    talent_pipeline = models.JSONField(default=dict, blank=True, help_text="Talent pipeline analysis")
    salary_projections = models.DecimalField(max_digits=10, decimal_places=2, default=0, help_text="Projected salary range")
    training_requirements = models.TextField(blank=True, help_text="Training and education requirements")
    certification_trends = models.JSONField(default=dict, blank=True, help_text="Certification requirement trends")
    remote_work_impact = models.FloatField(default=0, help_text="Impact of remote/telehealth work")
    diversity_inclusion_goals = models.TextField(blank=True, help_text="Diversity and inclusion goals")
    sustainability_factors = models.JSONField(default=dict, blank=True, help_text="Sustainability and ESG factors")
    validation_metrics = models.JSONField(default=dict, blank=True, help_text="Model validation metrics")
    update_frequency = models.CharField(max_length=20, choices=[
        ('monthly', 'Monthly'),
        ('quarterly', 'Quarterly'),
        ('semi_annual', 'Semi-Annual'),
        ('annual', 'Annual'),
    ], default='quarterly')
    last_validated = models.DateTimeField(null=True, blank=True)
    next_update = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Forecast: {self.get_specialty_display()} - {self.forecast_year}"

    class Meta:
        ordering = ['-generated_date']
