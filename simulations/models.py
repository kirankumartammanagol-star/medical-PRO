from django.db import models
from django.contrib.auth.models import User


class Simulation(models.Model):
    SCENARIO_TYPES = [
        ('emergency', 'Emergency Response'),
        ('diagnosis', 'Diagnostic Scenario'),
        ('patient_care', 'Patient Care Management'),
        ('surgical', 'Surgical Decision Making'),
        ('medication', 'Medication Management'),
        ('triage', 'Triage Assessment'),
        ('communication', 'Patient Communication'),
        ('ethics', 'Ethical Dilemma'),
        ('critical_care', 'Critical Care Management'),
        ('pediatric', 'Pediatric Emergency'),
        ('cardiac', 'Cardiac Emergency'),
        ('trauma', 'Trauma Management'),
    ]

    DIFFICULTY_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
        ('expert', 'Expert'),
    ]

    title = models.CharField(max_length=200)
    scenario_type = models.CharField(max_length=20, choices=SCENARIO_TYPES)
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES, default='intermediate')
    description = models.TextField()
    patient_name = models.CharField(max_length=100, default='Patient')
    patient_age = models.IntegerField(default=45)
    patient_gender = models.CharField(max_length=10, default='Male')
    patient_history = models.TextField(blank=True)
    presenting_symptoms = models.TextField()
    vital_signs = models.TextField(blank=True, help_text="JSON format vital signs data")
    lab_results = models.TextField(blank=True, help_text="JSON format lab results")
    correct_diagnosis = models.CharField(max_length=200, blank=True)
    expected_actions = models.TextField(help_text="Expected clinical actions, one per line")
    time_limit_minutes = models.IntegerField(default=30)
    icon = models.CharField(max_length=50, default='fa-heartbeat')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    # Enhanced virtual patient simulation fields
    patient_complaint = models.TextField(blank=True, help_text="Chief complaint in patient's own words")
    medical_history = models.TextField(blank=True, help_text="Comprehensive medical history")
    medications = models.TextField(blank=True, help_text="Current medications and allergies")
    social_history = models.TextField(blank=True, help_text="Social and lifestyle history")
    family_history = models.TextField(blank=True, help_text="Family medical history")
    physical_exam_findings = models.TextField(blank=True, help_text="Physical examination findings")
    imaging_results = models.TextField(blank=True, help_text="Imaging and diagnostic test results")
    treatment_plan = models.TextField(blank=True, help_text="Expected treatment plan")
    differential_diagnosis = models.TextField(blank=True, help_text="Differential diagnosis options")
    red_flags = models.TextField(blank=True, help_text="Critical red flags in presentation")
    educational_objectives = models.TextField(blank=True, help_text="Learning objectives for the simulation")
    clinical_guidelines = models.TextField(blank=True, help_text="Relevant clinical guidelines")
    scoring_rubric = models.JSONField(default=dict, blank=True, help_text="Scoring criteria for evaluation")
    adaptive_difficulty = models.BooleanField(default=False, help_text="Adaptive difficulty based on performance")
    vr_supported = models.BooleanField(default=False, help_text="Virtual Reality support available")
    ar_supported = models.BooleanField(default=False, help_text="Augmented Reality support available")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['scenario_type', 'difficulty']


class SimulationStep(models.Model):
    simulation = models.ForeignKey(Simulation, on_delete=models.CASCADE, related_name='steps')
    step_number = models.IntegerField(default=1)
    description = models.TextField()
    question = models.TextField()
    option_a = models.CharField(max_length=300)
    option_b = models.CharField(max_length=300)
    option_c = models.CharField(max_length=300)
    option_d = models.CharField(max_length=300)
    correct_option = models.CharField(max_length=1, choices=[('A','A'),('B','B'),('C','C'),('D','D')])
    feedback_correct = models.TextField(blank=True)
    feedback_incorrect = models.TextField(blank=True)
    
    # Enhanced simulation step fields
    step_type = models.CharField(max_length=20, choices=[
        ('assessment', 'Patient Assessment'),
        ('diagnosis', 'Diagnostic Decision'),
        ('treatment', 'Treatment Planning'),
        ('communication', 'Patient Communication'),
        ('documentation', 'Clinical Documentation'),
        ('medication', 'Medication Management'),
        ('procedure', 'Clinical Procedure'),
        ('emergency', 'Emergency Response'),
    ], default='assessment')
    time_limit_seconds = models.IntegerField(default=60)
    critical_step = models.BooleanField(default=False, help_text="Critical step for patient safety")
    hints_available = models.IntegerField(default=0, help_text="Number of hints available")
    required_equipment = models.TextField(blank=True, help_text="Equipment needed for this step")
    clinical_reasoning = models.TextField(blank=True, help_text="Clinical reasoning behind the correct answer")
    alternative_approaches = models.TextField(blank=True, help_text="Alternative acceptable approaches")
    common_errors = models.TextField(blank=True, help_text="Common mistakes to avoid")
    reference_materials = models.TextField(blank=True, help_text="Reference materials for this step")
    multimedia_content = models.JSONField(default=dict, blank=True, help_text="Images, videos, or audio content")
    interactive_elements = models.JSONField(default=list, blank=True, help_text="Interactive components")
    
    class Meta:
        ordering = ['step_number']


class SimulationAttempt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='simulation_attempts')
    simulation = models.ForeignKey(Simulation, on_delete=models.CASCADE, related_name='attempts')
    responses = models.JSONField(default=dict, blank=True)
    score = models.FloatField(default=0)
    percentage = models.FloatField(default=0)
    feedback = models.TextField(blank=True)
    time_taken_minutes = models.IntegerField(default=0)
    completed_at = models.DateTimeField(auto_now_add=True)
    
    # Enhanced simulation attempt fields
    clinical_reasoning_score = models.FloatField(default=0, help_text="Score for clinical reasoning")
    decision_making_score = models.FloatField(default=0, help_text="Score for clinical decisions")
    communication_score = models.FloatField(default=0, help_text="Score for patient communication")
    time_efficiency_score = models.FloatField(default=0, help_text="Score for time management")
    critical_steps_correct = models.IntegerField(default=0, help_text="Number of critical steps completed correctly")
    hints_used = models.IntegerField(default=0, help_text="Number of hints used during simulation")
    patient_outcome = models.CharField(max_length=50, choices=[
        ('excellent', 'Excellent Outcome'),
        ('good', 'Good Outcome'),
        ('fair', 'Fair Outcome'),
        ('poor', 'Poor Outcome'),
        ('critical', 'Critical Outcome'),
    ], default='good')
    competency_assessment = models.JSONField(default=dict, blank=True, help_text="Assessment by competency area")
    recommended_improvements = models.JSONField(default=list, blank=True, help_text="Areas for improvement")
    performance_trends = models.JSONField(default=dict, blank=True, help_text="Performance trend analysis")
    interview_score = models.FloatField(default=0, help_text="Overall interview performance score")
    hiring_recommendation = models.CharField(max_length=20, choices=[
        ('highly_recommended', 'Highly Recommended'),
        ('recommended', 'Recommended'),
        ('conditional', 'Conditional Recommendation'),
        ('not_recommended', 'Not Recommended'),
    ], blank=True)
    feedback_for_employer = models.TextField(blank=True, help_text="Feedback summary for hiring managers")
    simulation_mode = models.CharField(max_length=20, choices=[
        ('practice', 'Practice Mode'),
        ('assessment', 'Assessment Mode'),
        ('interview', 'Interview Mode'),
        ('training', 'Training Mode'),
    ], default='practice')
    difficulty_adjusted = models.BooleanField(default=False, help_text="Difficulty was adjusted during simulation")
    stress_level_assessed = models.BooleanField(default=False, help_text="Stress level was assessed")

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.simulation.title}: {self.percentage}%"

    class Meta:
        ordering = ['-completed_at']
