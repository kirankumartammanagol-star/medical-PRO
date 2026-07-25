import json
import requests
from datetime import datetime, date
from typing import Dict, Tuple, Optional
from django.conf import settings
from django.utils import timezone

class CredentialVerificationService:
    """
    Service for automatic verification of healthcare credentials
    Integrates with various medical board and certification databases
    """
    
    def __init__(self):
        self.api_endpoints = {
            'medical_license': {
                'california': 'https://www.mbc.ca.gov/api/license/verify',
                'new_york': 'https://www.nysed.gov/opd/verify',
                'texas': 'https://www.tmb.state.tx.us/api/verify',
                'florida': 'https://flhealthsource.gov/verify/api',
                # Add more state medical boards
            },
            'nursing_license': {
                'california': 'https://www.rn.ca.gov/api/verify',
                'new_york': 'https://www.op.nysed.gov/api/nursing/verify',
                'texas': 'https://www.bon.texas.gov/api/verify',
                'florida': 'https://floridasnursing.gov/api/verify',
                # Add more state nursing boards
            },
            'pharmacy_license': {
                'california': 'https://www.pharmacy.ca.gov/api/verify',
                'new_york': 'https://www.op.nysed.gov/api/pharmacy/verify',
                'texas': 'https://www.tsbp.state.tx.us/api/verify',
                # Add more state pharmacy boards
            },
            'board_certification': {
                'abms': 'https://www.certificationmatters.org/api/verify',
                'abim': 'https://www.abim.org/api/verify',
                'abs': 'https://www.absurgery.org/api/verify',
                # Add more specialty boards
            },
            'specialty_certification': {
                'aha': 'https://www.cpr.heart.org/api/verify',
                'ancc': 'https://www.nursingworld.org/api/verify',
                'aapc': 'https://www.aapc.com/api/verify',
                'ahima': 'https://www.ahima.org/api/verify',
                # Add more certification bodies
            }
        }
        
        self.headers = {
            'User-Agent': 'HealthcarePortal/1.0',
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
    
    def verify_credential(self, credential_type: str, license_number: str, 
                          issuing_state: str = None, issuing_authority: str = None,
                          additional_data: Dict = None) -> Tuple[bool, float, Dict]:
        """
        Verify a credential against appropriate databases
        
        Args:
            credential_type: Type of credential (medical_license, nursing_license, etc.)
            license_number: License/certification number
            issuing_state: State that issued the license (if applicable)
            issuing_authority: Authority that issued the credential
            additional_data: Additional data for verification
            
        Returns:
            Tuple of (success: bool, confidence_score: float, response_data: Dict)
        """
        
        if credential_type == 'medical_license':
            return self._verify_medical_license(license_number, issuing_state, additional_data)
        elif credential_type == 'nursing_license':
            return self._verify_nursing_license(license_number, issuing_state, additional_data)
        elif credential_type == 'pharmacy_license':
            return self._verify_pharmacy_license(license_number, issuing_state, additional_data)
        elif credential_type == 'board_certification':
            return self._verify_board_certification(license_number, issuing_authority, additional_data)
        elif credential_type in ['specialty_certification', 'acls_certification', 'cpr_certification']:
            return self._verify_specialty_certification(license_number, issuing_authority, additional_data)
        else:
            return False, 0.0, {"error": f"Unsupported credential type: {credential_type}"}
    
    def _verify_medical_license(self, license_number: str, state: str, data: Dict = None) -> Tuple[bool, float, Dict]:
        """Verify medical license with state medical board"""
        
        # In production, this would make actual API calls
        # For demo purposes, we'll simulate the verification
        
        state = state.lower() if state else ''
        
        # Simulate API response based on license number pattern
        mock_response = {
            "license_number": license_number,
            "status": "Active",
            "verification_date": timezone.now().isoformat(),
            "source": f"{state.title()} Medical Board",
            "physician_name": data.get('physician_name', 'Verified Physician') if data else 'Verified Physician',
            "specialty": data.get('specialty', 'General Practice') if data else 'General Practice',
            "issue_date": data.get('issue_date', '2020-01-01') if data else '2020-01-01',
            "expiry_date": data.get('expiry_date', '2025-12-31') if data else '2025-12-31',
            "disciplinary_actions": False,
            "board_sanctions": False,
            "verification_confidence": 95.0
        }
        
        # Simulate different scenarios based on license number
        if license_number.endswith('-SUSPENDED'):
            mock_response["status"] = "Suspended"
            mock_response["disciplinary_actions"] = True
            confidence = 70.0
        elif license_number.endswith('-EXPIRED'):
            mock_response["status"] = "Expired"
            confidence = 60.0
        else:
            confidence = 95.0
        
        success = mock_response["status"] in ["Active", "Current"]
        
        return success, confidence, mock_response
    
    def _verify_nursing_license(self, license_number: str, state: str, data: Dict = None) -> Tuple[bool, float, Dict]:
        """Verify nursing license with state nursing board"""
        
        mock_response = {
            "license_number": license_number,
            "status": "Active",
            "verification_date": timezone.now().isoformat(),
            "source": f"{state.title()} Board of Nursing",
            "nurse_name": data.get('nurse_name', 'Verified Nurse') if data else 'Verified Nurse',
            "license_type": data.get('license_type', 'RN') if data else 'RN',
            "specialty": data.get('specialty', 'General Nursing') if data else 'General Nursing',
            "issue_date": data.get('issue_date', '2020-01-01') if data else '2020-01-01',
            "expiry_date": data.get('expiry_date', '2024-12-31') if data else '2024-12-31',
            "disciplinary_actions": False,
            "verification_confidence": 92.0
        }
        
        if license_number.endswith('-DELINQUENT'):
            mock_response["status"] = "Delinquent"
            confidence = 65.0
        elif license_number.endswith('-SUSPENDED'):
            mock_response["status"] = "Suspended"
            mock_response["disciplinary_actions"] = True
            confidence = 70.0
        else:
            confidence = 92.0
        
        success = mock_response["status"] in ["Active", "Current"]
        
        return success, confidence, mock_response
    
    def _verify_pharmacy_license(self, license_number: str, state: str, data: Dict = None) -> Tuple[bool, float, Dict]:
        """Verify pharmacy license with state board of pharmacy"""
        
        mock_response = {
            "license_number": license_number,
            "status": "Active",
            "verification_date": timezone.now().isoformat(),
            "source": f"{state.title()} Board of Pharmacy",
            "pharmacist_name": data.get('pharmacist_name', 'Verified Pharmacist') if data else 'Verified Pharmacist',
            "pharmacy_degree": data.get('pharmacy_degree', 'PharmD') if data else 'PharmD',
            "issue_date": data.get('issue_date', '2020-01-01') if data else '2020-01-01',
            "expiry_date": data.get('expiry_date', '2024-12-31') if data else '2024-12-31',
            "dea_registration": data.get('dea_registration', f'BX{license_number[-7:]}') if data else f'BX{license_number[-7:]}',
            "disciplinary_actions": False,
            "verification_confidence": 94.0
        }
        
        if license_number.endswith('-PROBATION'):
            mock_response["status"] = "Probation"
            mock_response["disciplinary_actions"] = True
            confidence = 75.0
        else:
            confidence = 94.0
        
        success = mock_response["status"] in ["Active", "Current"]
        
        return success, confidence, mock_response
    
    def _verify_board_certification(self, cert_number: str, board: str, data: Dict = None) -> Tuple[bool, float, Dict]:
        """Verify board certification with specialty board"""
        
        mock_response = {
            "certification_id": cert_number,
            "status": "Certified",
            "verification_date": timezone.now().isoformat(),
            "source": board or "American Board of Medical Specialties",
            "physician_name": data.get('physician_name', 'Verified Physician') if data else 'Verified Physician',
            "specialty": data.get('specialty', 'Internal Medicine') if data else 'Internal Medicine',
            "subspecialty": data.get('subspecialty') if data else None,
            "certification_date": data.get('certification_date', '2018-01-01') if data else '2018-01-01',
            "expiry_date": data.get('expiry_date', '2028-12-31') if data else '2028-12-31',
            "maintenance_of_certification": True,
            "verification_confidence": 90.0
        }
        
        if cert_number.endswith('-EXPIRED'):
            mock_response["status"] = "Expired"
            confidence = 60.0
        elif cert_number.endswith('-REVOKED'):
            mock_response["status"] = "Revoked"
            confidence = 50.0
        else:
            confidence = 90.0
        
        success = mock_response["status"] in ["Certified", "Active"]
        
        return success, confidence, mock_response
    
    def _verify_specialty_certification(self, cert_number: str, organization: str, data: Dict = None) -> Tuple[bool, float, Dict]:
        """Verify specialty certification with certification body"""
        
        mock_response = {
            "certification_id": cert_number,
            "status": "Active",
            "verification_date": timezone.now().isoformat(),
            "source": organization or "Certification Authority",
            "holder_name": data.get('holder_name', 'Verified Professional') if data else 'Verified Professional',
            "certification_type": data.get('certification_type', 'Professional Certification') if data else 'Professional Certification',
            "issue_date": data.get('issue_date', '2022-01-01') if data else '2022-01-01',
            "expiry_date": data.get('expiry_date', '2025-01-01') if data else '2025-01-01',
            "verification_code": data.get('verification_code', f'VERIFY-{cert_number[-6:]}') if data else f'VERIFY-{cert_number[-6:]}',
            "verification_confidence": 88.0
        }
        
        if cert_number.endswith('-EXPIRED'):
            mock_response["status"] = "Expired"
            confidence = 55.0
        elif cert_number.endswith('-SUSPENDED'):
            mock_response["status"] = "Suspended"
            confidence = 65.0
        else:
            confidence = 88.0
        
        success = mock_response["status"] in ["Active", "Current", "Certified"]
        
        return success, confidence, mock_response
    
    def batch_verify_credentials(self, credentials: list) -> list:
        """Verify multiple credentials in batch"""
        
        results = []
        for credential in credentials:
            try:
                success, confidence, response = self.verify_credential(
                    credential.get('credential_type'),
                    credential.get('license_number'),
                    credential.get('issuing_state'),
                    credential.get('issuing_authority'),
                    credential
                )
                
                results.append({
                    'credential_id': credential.get('id'),
                    'success': success,
                    'confidence_score': confidence,
                    'verification_data': response,
                    'timestamp': timezone.now().isoformat()
                })
                
            except Exception as e:
                results.append({
                    'credential_id': credential.get('id'),
                    'success': False,
                    'confidence_score': 0.0,
                    'error': str(e),
                    'timestamp': timezone.now().isoformat()
                })
        
        return results
    
    def get_verification_status_summary(self, user_credentials) -> Dict:
        """Get summary of verification status for user's credentials"""
        
        total = len(user_credentials)
        verified = sum(1 for cred in user_credentials if cred.status == 'verified')
        auto_verified = sum(1 for cred in user_credentials if cred.auto_verified)
        expired = sum(1 for cred in user_credentials if cred.status == 'expired')
        pending = sum(1 for cred in user_credentials if cred.status == 'pending')
        
        avg_confidence = 0.0
        if total > 0:
            avg_confidence = sum(cred.verification_confidence_score for cred in user_credentials) / total
        
        return {
            'total_credentials': total,
            'verified_count': verified,
            'auto_verified_count': auto_verified,
            'expired_count': expired,
            'pending_count': pending,
            'verification_rate': (verified / total * 100) if total > 0 else 0,
            'average_confidence_score': avg_confidence,
            'last_updated': timezone.now().isoformat()
        }
