from django.db import models
from django.contrib.auth.models import User
from core.models import Hospital, MedicalCollege


class JobListing(models.Model):
    JOB_TYPES = [
        ('full_time', 'Full Time'),
        ('part_time', 'Part Time'),
        ('contract', 'Contract'),
        ('internship', 'Internship'),
        ('fellowship', 'Fellowship'),
        ('residency', 'Residency'),
        ('locum', 'Locum Tenens'),
    ]

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
        ('nursing', 'Nursing'),
        ('pharmacy', 'Pharmacy'),
        ('lab_technician', 'Lab Technician'),
        ('administration', 'Hospital Administration'),
    ]

    EXPERIENCE_LEVELS = [
        ('entry', 'Entry Level (0-2 years)'),
        ('mid', 'Mid Level (3-5 years)'),
        ('senior', 'Senior Level (5-10 years)'),
        ('expert', 'Expert Level (10+ years)'),
    ]

    title = models.CharField(max_length=200)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name='jobs', null=True, blank=True)
    hospital_name = models.CharField(max_length=200, default='Healthcare Institution')
    specialty = models.CharField(max_length=30, choices=SPECIALTY_CHOICES)
    job_type = models.CharField(max_length=20, choices=JOB_TYPES, default='full_time')
    experience_level = models.CharField(max_length=10, choices=EXPERIENCE_LEVELS, default='mid')
    location = models.CharField(max_length=200)
    description = models.TextField()
    requirements = models.TextField()
    credentials_required = models.TextField(blank=True, help_text="Required credentials/certifications")
    salary_min = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    salary_max = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    benefits = models.TextField(blank=True)
    posted_date = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_urgent = models.BooleanField(default=False)
    views_count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.title} - {self.hospital_name}"

    @property
    def salary_range(self):
        if self.salary_min and self.salary_max:
            return f"₹{self.salary_min:,.0f} - ₹{self.salary_max:,.0f}"
        return "Negotiable"

    class Meta:
        ordering = ['-posted_date']


class Application(models.Model):
    STATUS_CHOICES = [
        ('applied', 'Applied'),
        ('reviewing', 'Under Review'),
        ('shortlisted', 'Shortlisted'),
        ('interview', 'Interview Scheduled'),
        ('offered', 'Offer Made'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
        ('withdrawn', 'Withdrawn'),
    ]

    job = models.ForeignKey(JobListing, on_delete=models.CASCADE, related_name='applications')
    candidate = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applications')
    cover_letter = models.TextField(blank=True)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='applied')
    applied_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.candidate.get_full_name()} → {self.job.title}"

    class Meta:
        ordering = ['-applied_date']
        unique_together = ['job', 'candidate']


class Partnership(models.Model):
    PROGRAM_TYPES = [
        ('internship', 'Internship Program'),
        ('residency', 'Residency Program'),
        ('fellowship', 'Fellowship Program'),
        ('clinical_rotation', 'Clinical Rotation'),
        ('research', 'Research Collaboration'),
        ('recruitment', 'Direct Recruitment Pipeline'),
    ]

    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name='partnerships', null=True, blank=True)
    hospital_name = models.CharField(max_length=200, default='Hospital')
    college = models.ForeignKey(MedicalCollege, on_delete=models.CASCADE, related_name='partnerships', null=True, blank=True)
    college_name = models.CharField(max_length=200, default='Medical College')
    program_type = models.CharField(max_length=20, choices=PROGRAM_TYPES)
    description = models.TextField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    students_enrolled = models.IntegerField(default=0)
    placement_rate = models.FloatField(default=0, help_text="Percentage")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.hospital_name} ↔ {self.college_name} ({self.get_program_type_display()})"

    class Meta:
        ordering = ['-start_date']
