from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('doctor', 'Doctor'),
        ('nurse', 'Nurse'),
        ('technician', 'Lab Technician'),
        ('pharmacist', 'Pharmacist'),
        ('admin_staff', 'Administrative Staff'),
        ('student', 'Medical Student'),
        ('hospital_admin', 'Hospital Administrator'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='doctor')
    specialization = models.CharField(max_length=100, blank=True)
    experience_years = models.IntegerField(default=0)
    phone = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    profile_image = models.ImageField(upload_to='profiles/', blank=True, null=True)
    bio = models.TextField(blank=True)
    date_joined_portal = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.get_role_display()}"

    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'


class Hospital(models.Model):
    HOSPITAL_TYPES = [
        ('government', 'Government Hospital'),
        ('private', 'Private Hospital'),
        ('teaching', 'Teaching Hospital'),
        ('specialty', 'Specialty Hospital'),
        ('clinic', 'Clinic'),
    ]

    name = models.CharField(max_length=200)
    hospital_type = models.CharField(max_length=20, choices=HOSPITAL_TYPES)
    location = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    beds_count = models.IntegerField(default=0)
    departments = models.TextField(help_text="Comma-separated department names")
    established_year = models.IntegerField(default=2000)
    website = models.URLField(blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=15, blank=True)
    description = models.TextField(blank=True)
    logo = models.ImageField(upload_to='hospitals/', blank=True, null=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class MedicalCollege(models.Model):
    name = models.CharField(max_length=200)
    university = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    courses_offered = models.TextField(help_text="Comma-separated course names")
    accreditation = models.CharField(max_length=100, blank=True)
    established_year = models.IntegerField(default=2000)
    website = models.URLField(blank=True)
    email = models.EmailField(blank=True)
    total_students = models.IntegerField(default=0)
    placement_rate = models.FloatField(default=0.0, help_text="Percentage")
    description = models.TextField(blank=True)
    logo = models.ImageField(upload_to='colleges/', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.subject}"
