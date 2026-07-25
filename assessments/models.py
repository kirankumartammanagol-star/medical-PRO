from django.db import models
from django.contrib.auth.models import User


class Assessment(models.Model):
    CATEGORY_CHOICES = [
        ('patient_care', 'Patient Care Procedures'),
        ('medical_terminology', 'Medical Terminology'),
        ('clinical_decision', 'Clinical Decision Making'),
        ('emergency_response', 'Emergency Response'),
        ('nursing_fundamentals', 'Nursing Fundamentals'),
        ('pharmacology', 'Pharmacology Basics'),
        ('icd10_coding', 'ICD-10 Medical Coding'),
        ('snomed_ct', 'SNOMED CT Concepts'),
        ('hipaa_privacy', 'HIPAA & Patient Privacy'),
        ('infection_control', 'Infection Control & Safety'),
        ('emr_records', 'Electronic Medical Records (EMR)'),
        ('hl7_fhir', 'HL7 FHIR Interoperability'),
        ('lab_procedures', 'Laboratory Procedures'),
        ('ethics_compliance', 'Healthcare Ethics & Compliance'),
        ('hospital_admin', 'Hospital Administration & Workflow'),
    ]

    DIFFICULTY_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
        ('expert', 'Expert'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES, default='intermediate')
    time_limit_minutes = models.IntegerField(default=30)
    passing_score = models.IntegerField(default=70, help_text="Percentage required to pass")
    total_questions = models.IntegerField(default=10)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    icon = models.CharField(max_length=50, default='fa-clipboard-check')
    
    # Enhanced clinical assessment fields
    clinical_domain = models.CharField(max_length=100, blank=True, help_text="Clinical domain (e.g., Cardiology, Pediatrics)")
    terminology_standard = models.CharField(max_length=50, blank=True, choices=[
        ('icd10', 'ICD-10'),
        ('snomed_ct', 'SNOMED CT'),
        ('loinc', 'LOINC'),
        ('rxnorm', 'RxNorm'),
        ('cpt', 'CPT Codes'),
    ])
    competency_level = models.CharField(max_length=20, choices=[
        ('basic', 'Basic Competency'),
        ('intermediate', 'Intermediate Competency'),
        ('advanced', 'Advanced Competency'),
        ('expert', 'Expert Level'),
    ], default='intermediate')
    requires_clinical_validation = models.BooleanField(default=False)
    validation_criteria = models.TextField(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['category', 'difficulty']


class Question(models.Model):
    QUESTION_TYPES = [
        ('mcq', 'Multiple Choice'),
        ('true_false', 'True/False'),
        ('short_answer', 'Short Answer'),
        ('clinical_case', 'Clinical Case Study'),
        ('coding_exercise', 'Coding Exercise'),
        ('terminology_mapping', 'Terminology Mapping'),
    ]

    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField()
    question_type = models.CharField(max_length=20, choices=QUESTION_TYPES, default='mcq')
    option_a = models.CharField(max_length=300, blank=True)
    option_b = models.CharField(max_length=300, blank=True)
    option_c = models.CharField(max_length=300, blank=True)
    option_d = models.CharField(max_length=300, blank=True)
    correct_answer = models.CharField(max_length=300)
    explanation = models.TextField(blank=True)
    points = models.IntegerField(default=1)
    order = models.IntegerField(default=0)
    
    # Enhanced clinical question fields
    clinical_scenario = models.TextField(blank=True, help_text="Clinical context for the question")
    terminology_codes = models.JSONField(default=dict, blank=True, help_text="Related medical codes (ICD-10, SNOMED CT, etc.)")
    reference_materials = models.TextField(blank=True, help_text="Reference guidelines or literature")
    difficulty_weight = models.FloatField(default=1.0, help_text="Weight for adaptive testing")
    competency_tag = models.CharField(max_length=100, blank=True, help_text="Specific competency being tested")

    def __str__(self):
        return f"Q{self.order}: {self.text[:50]}"

    class Meta:
        ordering = ['order']


class AssessmentResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assessment_results')
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE, related_name='results')
    score = models.FloatField(default=0)
    total_points = models.IntegerField(default=0)
    percentage = models.FloatField(default=0)
    passed = models.BooleanField(default=False)
    time_taken_minutes = models.IntegerField(default=0)
    completed_at = models.DateTimeField(auto_now_add=True)
    answers = models.JSONField(default=dict, blank=True)
    
    # Enhanced result tracking
    competency_scores = models.JSONField(default=dict, blank=True, help_text="Scores by competency area")
    clinical_reasoning_score = models.FloatField(default=0, help_text="Score for clinical reasoning questions")
    terminology_accuracy = models.FloatField(default=0, help_text="Accuracy in medical terminology")
    adaptive_difficulty_achieved = models.CharField(max_length=20, blank=True)
    recommended_next_assessments = models.JSONField(default=list, blank=True)
    clinical_validation_required = models.BooleanField(default=False)
    validation_notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.assessment.title}: {self.percentage}%"

    class Meta:
        ordering = ['-completed_at']


class Certificate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='certificates')
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE)
    result = models.OneToOneField(AssessmentResult, on_delete=models.CASCADE)
    issue_date = models.DateTimeField(auto_now_add=True)
    certificate_id = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return f"Certificate: {self.user.username} - {self.assessment.title}"
