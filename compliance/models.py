from django.db import models
from django.contrib.auth.models import User


class ComplianceModule(models.Model):
    REGULATION_CHOICES = [
        ('hipaa', 'HIPAA - Health Insurance Portability and Accountability Act'),
        ('hitech', 'HITECH Act'),
        ('gdpr_health', 'GDPR (Healthcare Data)'),
        ('osha', 'OSHA - Workplace Safety'),
        ('joint_commission', 'Joint Commission Standards'),
        ('cms', 'CMS Regulations'),
        ('state_regulations', 'State-Specific Regulations'),
        ('infection_control', 'Infection Control Standards'),
        ('patient_rights', 'Patient Rights & Ethics'),
        ('data_breach', 'Data Breach Notification'),
        ('telehealth', 'Telehealth Compliance'),
        ('research_ethics', 'Research Ethics (IRB)'),
    ]

    title = models.CharField(max_length=200)
    regulation = models.CharField(max_length=30, choices=REGULATION_CHOICES)
    description = models.TextField()
    content = models.TextField(help_text="Training module content in HTML format")
    required_score = models.IntegerField(default=80)
    duration_minutes = models.IntegerField(default=60)
    is_mandatory = models.BooleanField(default=True)
    order = models.IntegerField(default=0)
    icon = models.CharField(max_length=50, default='fa-shield-alt')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Enhanced compliance module fields
    module_type = models.CharField(max_length=20, choices=[
        ('training', 'Training Module'),
        ('assessment', 'Assessment Only'),
        ('certification', 'Certification Program'),
        ('refresher', 'Refresher Course'),
    ], default='training')
    learning_objectives = models.TextField(blank=True, help_text="Learning objectives, one per line")
    target_audience = models.CharField(max_length=200, blank=True, help_text="Target audience roles")
    accreditation = models.CharField(max_length=100, blank=True, help_text="Accreditation body")
    ce_credits = models.FloatField(default=0, help_text="Continuing education credits")
    renewal_period_months = models.IntegerField(default=12, help_text="Renewal period in months")
    interactive_elements = models.JSONField(default=list, blank=True, help_text="Interactive components")
    case_studies = models.TextField(blank=True, help_text="Relevant case studies")

    def __str__(self):
        return f"{self.title} ({self.get_regulation_display()})"

    class Meta:
        ordering = ['order']


class ComplianceQuiz(models.Model):
    module = models.ForeignKey(ComplianceModule, on_delete=models.CASCADE, related_name='quizzes')
    question = models.TextField()
    option_a = models.CharField(max_length=300)
    option_b = models.CharField(max_length=300)
    option_c = models.CharField(max_length=300)
    option_d = models.CharField(max_length=300)
    correct_answer = models.CharField(max_length=1, choices=[('A','A'),('B','B'),('C','C'),('D','D')])
    explanation = models.TextField(blank=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return f"Quiz Q{self.order}: {self.question[:50]}"

    class Meta:
        ordering = ['order']
        verbose_name_plural = 'Compliance Quizzes'


class ComplianceRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='compliance_records')
    module = models.ForeignKey(ComplianceModule, on_delete=models.CASCADE, related_name='records')
    score = models.FloatField(default=0)
    percentage = models.FloatField(default=0)
    passed = models.BooleanField(default=False)
    completion_date = models.DateTimeField(auto_now_add=True)
    expiry_date = models.DateField(null=True, blank=True)
    certificate_id = models.CharField(max_length=50, blank=True)
    
    # Enhanced compliance record fields
    training_progress = models.JSONField(default=dict, blank=True, help_text="Progress tracking data")
    time_spent_minutes = models.IntegerField(default=0)
    quiz_attempts = models.IntegerField(default=1)
    weak_areas = models.JSONField(default=list, blank=True, help_text="Areas needing improvement")
    remediation_required = models.BooleanField(default=False)
    remediation_completed = models.BooleanField(default=False)
    audit_trail = models.JSONField(default=list, blank=True, help_text="Audit trail of compliance activities")
    supervisor_approval = models.BooleanField(default=False)
    approved_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='approved_compliance')
    compliance_score = models.FloatField(default=0, help_text="Overall compliance score")
    last_review_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.module.title}: {'Passed' if self.passed else 'Failed'}"

    class Meta:
        ordering = ['-completion_date']
