from django.db import models
from django.contrib.auth.models import User


class EMRSystem(models.Model):
    name = models.CharField(max_length=200)
    vendor = models.CharField(max_length=200)
    version = models.CharField(max_length=50, blank=True)
    description = models.TextField()
    features = models.TextField(help_text="Key features, comma-separated")
    interoperability_standards = models.CharField(max_length=200, default='HL7 FHIR')
    market_share = models.FloatField(default=0, help_text="Percentage")
    logo = models.ImageField(upload_to='emr_systems/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    
    # Enhanced EMR system fields
    fhir_version = models.CharField(max_length=20, default='R4', help_text="FHIR version supported")
    hl7_v2_compliance = models.BooleanField(default=True)
    api_endpoints = models.JSONField(default=dict, blank=True, help_text="Available API endpoints")
    certification_status = models.CharField(max_length=100, blank=True, help_text="ONC/other certifications")
    deployment_type = models.CharField(max_length=50, choices=[
        ('cloud', 'Cloud-based'),
        ('on_premise', 'On-premise'),
        ('hybrid', 'Hybrid'),
    ], default='cloud')
    specialty_focus = models.CharField(max_length=200, blank=True, help_text="Specialty areas served")

    def __str__(self):
        return f"{self.name} ({self.vendor})"

    class Meta:
        verbose_name = 'EMR System'
        ordering = ['name']


class CompetencyTest(models.Model):
    STANDARD_CHOICES = [
        ('hl7_fhir', 'HL7 FHIR'),
        ('hl7_v2', 'HL7 v2'),
        ('dicom', 'DICOM'),
        ('cda', 'CDA (Clinical Document Architecture)'),
        ('general_emr', 'General EMR Usage'),
        ('data_entry', 'Clinical Data Entry'),
        ('reporting', 'Clinical Reporting'),
        ('fhir_resources', 'FHIR Resources'),
        ('fhir_apis', 'FHIR API Integration'),
        ('interoperability', 'Healthcare Interoperability'),
        ('clinical_workflow', 'Clinical Workflow Management'),
        ('patient_portal', 'Patient Portal Management'),
    ]

    emr_system = models.ForeignKey(EMRSystem, on_delete=models.CASCADE, related_name='tests', null=True, blank=True)
    title = models.CharField(max_length=200)
    standard = models.CharField(max_length=30, choices=STANDARD_CHOICES, default='general_emr')
    description = models.TextField()
    passing_score = models.IntegerField(default=70)
    time_limit_minutes = models.IntegerField(default=45)
    total_questions = models.IntegerField(default=15)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    # Enhanced competency test fields
    practical_component = models.BooleanField(default=False, help_text="Includes hands-on EMR simulation")
    simulation_scenario = models.TextField(blank=True, help_text="Description of practical simulation")
    required_certifications = models.JSONField(default=list, blank=True, help_text="Required certifications")
    skill_level = models.CharField(max_length=20, choices=[
        ('basic', 'Basic User'),
        ('intermediate', 'Intermediate User'),
        ('advanced', 'Advanced User'),
        ('expert', 'Expert/Superuser'),
    ], default='intermediate')
    test_environment = models.CharField(max_length=100, blank=True, help_text="Test EMR environment details")

    def __str__(self):
        return self.title


class CompetencyQuestion(models.Model):
    test = models.ForeignKey(CompetencyTest, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField()
    option_a = models.CharField(max_length=300)
    option_b = models.CharField(max_length=300)
    option_c = models.CharField(max_length=300)
    option_d = models.CharField(max_length=300)
    correct_answer = models.CharField(max_length=1, choices=[('A','A'),('B','B'),('C','C'),('D','D')])
    explanation = models.TextField(blank=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']


class CompetencyResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='emr_results')
    test = models.ForeignKey(CompetencyTest, on_delete=models.CASCADE, related_name='results')
    score = models.FloatField(default=0)
    percentage = models.FloatField(default=0)
    certified = models.BooleanField(default=False)
    completed_at = models.DateTimeField(auto_now_add=True)
    certificate_number = models.CharField(max_length=50, blank=True)
    
    # Enhanced competency result fields
    practical_score = models.FloatField(default=0, help_text="Score for practical simulation component")
    theoretical_score = models.FloatField(default=0, help_text="Score for theoretical questions")
    fhir_competency_score = models.FloatField(default=0, help_text="Specific FHIR competency score")
    workflow_efficiency = models.FloatField(default=0, help_text="Efficiency in clinical workflow tasks")
    error_rate = models.FloatField(default=0, help_text="Error rate in simulation")
    time_efficiency = models.FloatField(default=0, help_text="Time-based efficiency score")
    recommended_training = models.JSONField(default=list, blank=True, help_text="Recommended training modules")
    skill_gaps = models.JSONField(default=list, blank=True, help_text="Identified skill gaps")
    next_renewal_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.test.title}: {'Certified' if self.certified else 'Not Certified'}"

    class Meta:
        ordering = ['-completed_at']
