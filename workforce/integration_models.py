from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class HealthcareInstitution(models.Model):
    """Model for healthcare institutions (hospitals, clinics, etc.)"""
    
    INSTITUTION_TYPES = [
        ('hospital', 'Hospital'),
        ('clinic', 'Clinic'),
        ('nursing_home', 'Nursing Home'),
        ('rehabilitation', 'Rehabilitation Center'),
        ('mental_health', 'Mental Health Facility'),
        ('urgent_care', 'Urgent Care Center'),
        ('specialty_center', 'Specialty Center'),
        ('research_institute', 'Research Institute'),
    ]
    
    SIZES = [
        ('small', 'Small (<100 beds)'),
        ('medium', 'Medium (100-500 beds)'),
        ('large', 'Large (500-1000 beds)'),
        ('extra_large', 'Extra Large (>1000 beds)'),
    ]
    
    name = models.CharField(max_length=200)
    institution_type = models.CharField(max_length=30, choices=INSTITUTION_TYPES)
    size = models.CharField(max_length=20, choices=SIZES)
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100, default='India')
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    website = models.URLField(blank=True)
    
    # Healthcare specific fields
    bed_count = models.IntegerField(default=0)
    emergency_services = models.BooleanField(default=False)
    trauma_level = models.CharField(max_length=20, choices=[
        ('none', 'None'),
        ('level_3', 'Level 3'),
        ('level_2', 'Level 2'),
        ('level_1', 'Level 1'),
    ], default='none')
    teaching_hospital = models.BooleanField(default=False)
    accreditation = models.CharField(max_length=100, blank=True)
    specialties_offered = models.JSONField(default=list, blank=True)
    
    # Integration fields
    active_partnerships = models.BooleanField(default=False)
    partnership_coordinator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='coordinated_institutions')
    established_date = models.DateField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - {self.get_city_display()}"
    
    class Meta:
        ordering = ['name', 'city']


class EducationalInstitution(models.Model):
    """Model for educational institutions (medical colleges, nursing schools, etc.)"""
    
    INSTITUTION_TYPES = [
        ('medical_college', 'Medical College'),
        ('nursing_school', 'Nursing School'),
        ('pharmacy_college', 'Pharmacy College'),
        ('allied_health', 'Allied Health College'),
        ('university', 'University'),
        ('technical_institute', 'Technical Institute'),
        ('vocational_school', 'Vocational School'),
        ('continuing_education', 'Continuing Education Center'),
    ]
    
    name = models.CharField(max_length=200)
    institution_type = models.CharField(max_length=30, choices=INSTITUTION_TYPES)
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100, default='India')
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    website = models.URLField(blank=True)
    
    # Education specific fields
    established_year = models.IntegerField()
    accreditation_body = models.CharField(max_length=100)
    programs_offered = models.JSONField(default=list, blank=True)
    annual_intake = models.IntegerField(default=0)
    current_enrollment = models.IntegerField(default=0)
    graduation_rate = models.FloatField(default=0.0)
    placement_rate = models.FloatField(default=0.0)
    
    # Clinical training fields
    clinical_training_required = models.BooleanField(default=True)
    clinical_hours_required = models.IntegerField(default=0)
    affiliated_hospitals = models.ManyToManyField(HealthcareInstitution, blank=True, related_name='affiliated_schools')
    
    # Integration fields
    active_partnerships = models.BooleanField(default=False)
    partnership_coordinator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='coordinated_schools')
    internship_program = models.BooleanField(default=False)
    residency_program = models.BooleanField(default=False)
    continuing_education_programs = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - {self.get_institution_type_display()}"
    
    class Meta:
        ordering = ['name', 'city']


class Partnership(models.Model):
    """Model for partnerships between healthcare and educational institutions"""
    
    PARTNERSHIP_TYPES = [
        ('clinical_training', 'Clinical Training'),
        ('internship', 'Internship Program'),
        ('residency', 'Residency Program'),
        ('research', 'Research Collaboration'),
        ('faculty_exchange', 'Faculty Exchange'),
        ('student_exchange', 'Student Exchange'),
        ('continuing_education', 'Continuing Education'),
        ('curriculum_development', 'Curriculum Development'),
        ('joint_programs', 'Joint Programs'),
        ('technology_transfer', 'Technology Transfer'),
    ]
    
    STATUS_CHOICES = [
        ('proposed', 'Proposed'),
        ('active', 'Active'),
        ('suspended', 'Suspended'),
        ('completed', 'Completed'),
        ('terminated', 'Terminated'),
    ]
    
    healthcare_institution = models.ForeignKey(HealthcareInstitution, on_delete=models.CASCADE, related_name='partnerships')
    educational_institution = models.ForeignKey(EducationalInstitution, on_delete=models.CASCADE, related_name='partnerships')
    partnership_type = models.CharField(max_length=30, choices=PARTNERSHIP_TYPES)
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='proposed')
    
    # Partnership details
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    duration_months = models.IntegerField(default=12)
    renewal_option = models.BooleanField(default=True)
    
    # Resource allocation
    annual_budget = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    healthcare_commitment = models.TextField(blank=True, help_text="Resources committed by healthcare institution")
    education_commitment = models.TextField(blank=True, help_text="Resources committed by educational institution")
    
    # Program details
    target_participants = models.IntegerField(default=0)
    actual_participants = models.IntegerField(default=0)
    completion_rate = models.FloatField(default=0.0)
    success_metrics = models.JSONField(default=dict, blank=True)
    
    # Contact information
    healthcare_contact = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='healthcare_partnerships')
    education_contact = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='education_partnerships')
    
    # Tracking and evaluation
    quarterly_reports = models.BooleanField(default=True)
    annual_evaluation = models.BooleanField(default=True)
    key_performance_indicators = models.JSONField(default=dict, blank=True)
    outcomes_measured = models.JSONField(default=list, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.healthcare_institution.name} - {self.educational_institution.name}: {self.get_partnership_type_display()}"
    
    class Meta:
        ordering = ['-created_at']


class StudentPlacement(models.Model):
    """Model for tracking student placements and career transitions"""
    
    PLACEMENT_TYPES = [
        ('internship', 'Internship'),
        ('clinical_rotation', 'Clinical Rotation'),
        ('residency', 'Residency'),
        ('employment', 'Employment'),
        ('fellowship', 'Fellowship'),
        ('research_position', 'Research Position'),
    ]
    
    STATUS_CHOICES = [
        ('applied', 'Applied'),
        ('interview', 'Interview Scheduled'),
        ('accepted', 'Accepted'),
        ('active', 'Active'),
        ('completed', 'Completed'),
        ('terminated', 'Terminated'),
        ('rejected', 'Rejected'),
    ]
    
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='placements')
    educational_institution = models.ForeignKey(EducationalInstitution, on_delete=models.CASCADE, related_name='student_placements')
    healthcare_institution = models.ForeignKey(HealthcareInstitution, on_delete=models.CASCADE, related_name='student_placements')
    placement_type = models.CharField(max_length=20, choices=PLACEMENT_TYPES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='applied')
    
    # Placement details
    department = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    supervisor = models.CharField(max_length=200, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    stipend_salary = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    # Academic information
    program = models.CharField(max_length=100)
    year_of_study = models.IntegerField()
    gpa = models.FloatField(null=True, blank=True)
    relevant_certifications = models.JSONField(default=list, blank=True)
    
    # Performance tracking
    performance_rating = models.FloatField(null=True, blank=True)
    supervisor_feedback = models.TextField(blank=True)
    skills_acquired = models.JSONField(default=list, blank=True)
    projects_completed = models.JSONField(default=list, blank=True)
    
    # Outcome tracking
    job_offer_received = models.BooleanField(default=False)
    job_offer_accepted = models.BooleanField(default=False)
    employment_details = models.JSONField(default=dict, blank=True)
    career_progression = models.JSONField(default=dict, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.student.get_full_name()} - {self.healthcare_institution.name} ({self.get_placement_type_display()})"
    
    class Meta:
        ordering = ['-created_at']


class CurriculumAlignment(models.Model):
    """Model for aligning educational curriculum with healthcare industry needs"""
    
    ALIGNMENT_TYPES = [
        ('skill_gap_analysis', 'Skill Gap Analysis'),
        ('curriculum_review', 'Curriculum Review'),
        ('competency_mapping', 'Competency Mapping'),
        ('industry_standards', 'Industry Standards Alignment'),
        ('technology_integration', 'Technology Integration'),
        ('certification_preparation', 'Certification Preparation'),
    ]
    
    educational_institution = models.ForeignKey(EducationalInstitution, on_delete=models.CASCADE, related_name='curriculum_alignments')
    healthcare_institution = models.ForeignKey(HealthcareInstitution, on_delete=models.CASCADE, related_name='curriculum_alignments')
    alignment_type = models.CharField(max_length=30, choices=ALIGNMENT_TYPES)
    
    # Alignment details
    program_name = models.CharField(max_length=100)
    course_code = models.CharField(max_length=20, blank=True)
    competency_area = models.CharField(max_length=100)
    industry_requirement = models.TextField()
    current_curriculum = models.TextField()
    recommended_changes = models.TextField()
    
    # Assessment and validation
    alignment_score = models.FloatField(default=0.0, help_text="Score from 0-100 indicating alignment level")
    gap_identified = models.BooleanField(default=False)
    priority_level = models.CharField(max_length=20, choices=[
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('critical', 'Critical'),
    ], default='medium')
    
    # Implementation tracking
    implementation_status = models.CharField(max_length=20, choices=[
        ('not_started', 'Not Started'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('on_hold', 'On Hold'),
    ], default='not_started')
    implementation_date = models.DateField(null=True, blank=True)
    responsible_party = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    
    # Impact assessment
    student_performance_impact = models.FloatField(null=True, blank=True)
    employer_satisfaction = models.FloatField(null=True, blank=True)
    placement_rate_impact = models.FloatField(null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.educational_institution.name} - {self.healthcare_institution.name}: {self.competency_area}"
    
    class Meta:
        ordering = ['-created_at']


class IntegrationMetrics(models.Model):
    """Model for tracking integration success metrics"""
    
    METRIC_TYPES = [
        ('placement_rate', 'Placement Rate'),
        ('retention_rate', 'Retention Rate'),
        ('satisfaction_score', 'Satisfaction Score'),
        ('skill_development', 'Skill Development'),
        ('time_to_productivity', 'Time to Productivity'),
        ('cost_effectiveness', 'Cost Effectiveness'),
        ('quality_improvement', 'Quality Improvement'),
        ('innovation_impact', 'Innovation Impact'),
    ]
    
    partnership = models.ForeignKey(Partnership, on_delete=models.CASCADE, related_name='metrics')
    metric_type = models.CharField(max_length=30, choices=METRIC_TYPES)
    measurement_period = models.CharField(max_length=20, help_text="e.g., Q1 2026, Annual 2025")
    
    # Metric values
    baseline_value = models.FloatField(default=0.0)
    current_value = models.FloatField(default=0.0)
    target_value = models.FloatField(default=0.0)
    percentage_change = models.FloatField(default=0.0)
    
    # Data sources and validation
    data_source = models.CharField(max_length=200)
    collection_method = models.CharField(max_length=100)
    confidence_level = models.FloatField(default=0.95)
    sample_size = models.IntegerField(default=0)
    
    # Analysis and insights
    trend_analysis = models.TextField(blank=True)
    key_insights = models.TextField(blank=True)
    recommendations = models.TextField(blank=True)
    
    # Benchmarking
    industry_benchmark = models.FloatField(null=True, blank=True)
    peer_comparison = models.JSONField(default=dict, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.partnership.title} - {self.get_metric_type_display()}: {self.measurement_period}"
    
    class Meta:
        ordering = ['-created_at']
