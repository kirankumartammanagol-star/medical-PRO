from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import requests
import json


class Credential(models.Model):
    CREDENTIAL_TYPES = [
        ('medical_license', 'Medical License'),
        ('nursing_license', 'Nursing License'),
        ('board_certification', 'Board Certification'),
        ('specialty_certification', 'Specialty Certification'),
        ('cpr_certification', 'CPR/BLS Certification'),
        ('acls_certification', 'ACLS Certification'),
        ('pharmacy_license', 'Pharmacy License'),
        ('technician_certification', 'Technician Certification'),
        ('residency_completion', 'Residency Completion'),
        ('fellowship', 'Fellowship Certificate'),
    ]

    STATUS_CHOICES = [
        ('pending', 'Pending Verification'),
        ('under_review', 'Under Review'),
        ('verified', 'Verified'),
        ('rejected', 'Rejected'),
        ('expired', 'Expired'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='credentials')
    credential_type = models.CharField(max_length=30, choices=CREDENTIAL_TYPES)
    title = models.CharField(max_length=200)
    license_number = models.CharField(max_length=100)
    issuing_authority = models.CharField(max_length=200)
    issuing_state = models.CharField(max_length=100, blank=True)
    issue_date = models.DateField()
    expiry_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    document = models.FileField(upload_to='credentials/', blank=True, null=True)
    notes = models.TextField(blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    verified_at = models.DateTimeField(null=True, blank=True)
    verified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='verified_credentials')
    
    # Enhanced verification fields
    auto_verified = models.BooleanField(default=False)
    verification_source = models.CharField(max_length=200, blank=True, help_text="Source of automatic verification")
    verification_api_response = models.JSONField(default=dict, blank=True)
    last_verification_attempt = models.DateTimeField(null=True, blank=True)
    verification_confidence_score = models.FloatField(default=0.0, help_text="Confidence score 0-100")
    external_verification_id = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.get_credential_type_display()}"

    @property
    def is_valid(self):
        from django.utils import timezone
        if self.expiry_date and self.expiry_date < timezone.now().date():
            return False
        return self.status == 'verified'
    
    def verify_with_external_api(self):
        """
        Automatic verification with external healthcare credential databases
        Returns (success: bool, confidence_score: float, response_data: dict)
        """
        try:
            # Simulate API calls to various medical boards
            if self.credential_type == 'medical_license':
                return self._verify_medical_license()
            elif self.credential_type == 'nursing_license':
                return self._verify_nursing_license()
            elif self.credential_type == 'board_certification':
                return self._verify_board_certification()
            else:
                return False, 0.0, {"error": "Unsupported credential type for auto-verification"}
        except Exception as e:
            return False, 0.0, {"error": str(e)}
    
    def _verify_medical_license(self):
        """Verify medical license with state medical boards"""
        # Mock API response - in production, integrate with real APIs
        mock_response = {
            "valid": True,
            "license_status": "Active",
            "issue_date": self.issue_date.strftime("%Y-%m-%d"),
            "expiry_date": self.expiry_date.strftime("%Y-%m-%d") if self.expiry_date else None,
            "physician_name": self.user.get_full_name(),
            "specialty": "General Practice",
            "board_sanctions": False,
            "malpractice_claims": 0
        }
        
        confidence = 95.0 if mock_response["valid"] else 0.0
        return True, confidence, mock_response
    
    def _verify_nursing_license(self):
        """Verify nursing license with state nursing boards"""
        mock_response = {
            "valid": True,
            "license_status": "Active",
            "license_type": "Registered Nurse",
            "nursing_specialty": "Medical-Surgical",
            "disciplinary_actions": False
        }
        
        confidence = 92.0 if mock_response["valid"] else 0.0
        return True, confidence, mock_response
    
    def _verify_board_certification(self):
        """Verify board certification with specialty boards"""
        mock_response = {
            "valid": True,
            "certification_status": "Active",
            "board_name": self.issuing_authority,
            "specialty": self.title,
            "certification_date": self.issue_date.strftime("%Y-%m-%d"),
            "maintenance_of_certification": True
        }
        
        confidence = 90.0 if mock_response["valid"] else 0.0
        return True, confidence, mock_response
    
    def schedule_reverification(self):
        """Schedule automatic reverification for credentials with expiry dates"""
        if self.expiry_date:
            # Schedule verification 30 days before expiry
            from datetime import timedelta
            notification_date = self.expiry_date - timedelta(days=30)
            return notification_date >= timezone.now().date()
        return False

    class Meta:
        ordering = ['-submitted_at']


class VerificationRequest(models.Model):
    credential = models.ForeignKey(Credential, on_delete=models.CASCADE, related_name='verification_requests')
    requested_by = models.ForeignKey(User, on_delete=models.CASCADE)
    verification_notes = models.TextField(blank=True)
    verification_status = models.CharField(max_length=20, choices=Credential.STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Verification: {self.credential.title}"
