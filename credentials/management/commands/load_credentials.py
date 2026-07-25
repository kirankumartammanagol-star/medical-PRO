from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from credentials.models import Credential
import json
import os
from datetime import datetime

class Command(BaseCommand):
    help = 'Load credential verification datasets into the database'

    def handle(self, *args, **options):
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        
        # Get or create a test user for credential assignments
        test_user, created = User.objects.get_or_create(
            username='test_healthcare_professional',
            defaults={
                'first_name': 'Test',
                'last_name': 'Professional',
                'email': 'test@healthcare.com',
                'is_staff': False,
                'is_active': True
            }
        )
        
        if created:
            test_user.set_password('testpass123')
            test_user.save()
            self.stdout.write(self.style.SUCCESS(f'Created test user: {test_user.username}'))
        
        # Load medical licenses
        self.load_medical_licenses(base_dir, test_user)
        
        # Load nursing licenses
        self.load_nursing_licenses(base_dir, test_user)
        
        # Load board certifications
        self.load_board_certifications(base_dir, test_user)
        
        # Load specialty certifications
        self.load_specialty_certifications(base_dir, test_user)
        
        # Load pharmacy licenses
        self.load_pharmacy_licenses(base_dir, test_user)
        
        self.stdout.write(self.style.SUCCESS('All credential datasets loaded successfully!'))

    def load_medical_licenses(self, base_dir, user):
        file_path = os.path.join(base_dir, 'medical_licenses.json')
        if not os.path.exists(file_path):
            self.stdout.write(self.style.WARNING(f'Medical licenses file not found: {file_path}'))
            return
        
        with open(file_path, 'r') as f:
            licenses = json.load(f)
        
        for license_data in licenses:
            credential = Credential.objects.create(
                user=user,
                credential_type='medical_license',
                title=f"Medical License - {license_data['specialty']}",
                license_number=license_data['license_number'],
                issuing_authority=f"{license_data['issuing_state']} Medical Board",
                issuing_state=license_data['issuing_state'],
                issue_date=datetime.strptime(license_data['issue_date'], '%Y-%m-%d').date(),
                expiry_date=datetime.strptime(license_data['expiry_date'], '%Y-%m-%d').date(),
                status='verified' if license_data['status'] == 'Active' else 'expired',
                notes=f"Physician: {license_data['physician_name']}\n"
                      f"Specialty: {license_data['specialty']}\n"
                      f"Board Certified: {license_data['board_certified']}\n"
                      f"DEA Registration: {license_data['dea_registration']}\n"
                      f"NPI Number: {license_data['npi_number']}\n"
                      f"Malpractice Claims: {license_data['malpractice_claims']}\n"
                      f"Disciplinary Actions: {license_data['disciplinary_actions']}",
                auto_verified=True,
                verification_source='State Medical Board Database',
                verification_confidence_score=95.0,
                verification_api_response=license_data
            )
            self.stdout.write(f'Created medical license credential: {credential.license_number}')

    def load_nursing_licenses(self, base_dir, user):
        file_path = os.path.join(base_dir, 'nursing_licenses.json')
        if not os.path.exists(file_path):
            self.stdout.write(self.style.WARNING(f'Nursing licenses file not found: {file_path}'))
            return
        
        with open(file_path, 'r') as f:
            licenses = json.load(f)
        
        for license_data in licenses:
            credential_type_map = {
                'RN': 'nursing_license',
                'LPN': 'nursing_license',
                'APRN': 'nursing_license',
                'CNS': 'nursing_license',
                'CNM': 'nursing_license',
                'CRNA': 'nursing_license'
            }
            
            credential = Credential.objects.create(
                user=user,
                credential_type=credential_type_map.get(license_data['license_type'], 'nursing_license'),
                title=f"{license_data['license_type']} License - {license_data['specialty']}",
                license_number=license_data['license_number'],
                issuing_authority=f"{license_data['issuing_state']} Board of Nursing",
                issuing_state=license_data['issuing_state'],
                issue_date=datetime.strptime(license_data['issue_date'], '%Y-%m-%d').date(),
                expiry_date=datetime.strptime(license_data['expiry_date'], '%Y-%m-%d').date(),
                status='verified' if license_data['status'] == 'Active' else 'expired',
                notes=f"Nurse: {license_data['nurse_name']}\n"
                      f"License Type: {license_data['license_type']}\n"
                      f"Specialty: {license_data['specialty']}\n"
                      f"Years Experience: {license_data['years_experience']}\n"
                      f"Current Employer: {license_data['current_employer']}\n"
                      f"BLS Certified: {license_data['bls_certified']}\n"
                      f"ACLS Certified: {license_data['acls_certified']}\n"
                      f"Advanced Certification: {license_data['advanced_certification']}\n"
                      f"Disciplinary Actions: {license_data['disciplinary_actions']}",
                auto_verified=True,
                verification_source='State Board of Nursing Database',
                verification_confidence_score=92.0,
                verification_api_response=license_data
            )
            self.stdout.write(f'Created nursing license credential: {credential.license_number}')

    def load_board_certifications(self, base_dir, user):
        file_path = os.path.join(base_dir, 'board_certifications.json')
        if not os.path.exists(file_path):
            self.stdout.write(self.style.WARNING(f'Board certifications file not found: {file_path}'))
            return
        
        with open(file_path, 'r') as f:
            certifications = json.load(f)
        
        for cert_data in certifications:
            credential = Credential.objects.create(
                user=user,
                credential_type='board_certification',
                title=f"Board Certification - {cert_data['specialty']}",
                license_number=cert_data['certification_id'],
                issuing_authority=cert_data['board_name'],
                issue_date=datetime.strptime(cert_data['certification_date'], '%Y-%m-%d').date(),
                expiry_date=datetime.strptime(cert_data['expiry_date'], '%Y-%m-%d').date(),
                status='verified' if cert_data['status'] == 'Certified' else 'expired',
                notes=f"Physician: {cert_data['physician_name']}\n"
                      f"Board: {cert_data['board_name']}\n"
                      f"Specialty: {cert_data['specialty']}\n"
                      f"Subspecialty: {cert_data['subspecialty'] or 'None'}\n"
                      f"Maintenance of Certification: {cert_data['maintenance_of_certification']}\n"
                      f"CME Credits Earned: {cert_data['cme_credits_earned']}\n"
                      f"Practice Address: {cert_data['practice_address']}",
                auto_verified=True,
                verification_source='Board Certification Database',
                verification_confidence_score=90.0,
                verification_api_response=cert_data
            )
            self.stdout.write(f'Created board certification: {credential.license_number}')

    def load_specialty_certifications(self, base_dir, user):
        file_path = os.path.join(base_dir, 'specialty_certifications.json')
        if not os.path.exists(file_path):
            self.stdout.write(self.style.WARNING(f'Specialty certifications file not found: {file_path}'))
            return
        
        with open(file_path, 'r') as f:
            certifications = json.load(f)
        
        # Map certification types to credential types
        cert_type_map = {
            'ACLS': 'acls_certification',
            'BLS': 'cpr_certification',
            'PALS': 'specialty_certification',
            'NRP': 'specialty_certification',
            'TNCC': 'specialty_certification',
            'ENPC': 'specialty_certification',
            'CEN': 'specialty_certification',
            'CCRN': 'specialty_certification',
            'CWCN': 'specialty_certification',
            'CNOR': 'specialty_certification',
            'CPhT': 'pharmacy_license',
            'CPhT-Adv': 'pharmacy_license',
            'RRT': 'technician_certification',
            'CRT': 'technician_certification',
            'RDCS': 'technician_certification',
            'RDMS': 'technician_certification',
            'CMT': 'technician_certification',
            'CMA': 'technician_certification',
            'RMA': 'technician_certification',
            'NCLEX': 'nursing_license',
            'CNS': 'nursing_license',
            'CNSC': 'nursing_license',
            'OCN': 'specialty_certification',
            'CPHQ': 'specialty_certification',
            'RHIA': 'technician_certification',
            'RHIT': 'technician_certification',
            'CCS': 'technician_certification',
            'CPC': 'technician_certification',
            'COC': 'technician_certification',
            'CRC': 'technician_certification'
        }
        
        for cert_data in certifications:
            credential_type = cert_type_map.get(cert_data['certification_type'], 'specialty_certification')
            
            credential = Credential.objects.create(
                user=user,
                credential_type=credential_type,
                title=f"{cert_data['certification_type']} Certification",
                license_number=cert_data['certification_id'],
                issuing_authority=cert_data['issuing_organization'],
                issue_date=datetime.strptime(cert_data['issue_date'], '%Y-%m-%d').date(),
                expiry_date=datetime.strptime(cert_data['expiry_date'], '%Y-%m-%d').date(),
                status='verified' if cert_data['status'] == 'Active' else 'expired',
                notes=f"Holder: {cert_data['holder_name']}\n"
                      f"Organization: {cert_data['issuing_organization']}\n"
                      f"Practice Area: {cert_data['practice_area']}\n"
                      f"Verification Code: {cert_data['verification_code']}\n"
                      f"Renewal Required: {cert_data['renewal_required']}\n"
                      f"CE Required: {cert_data['continuing_education_required']}",
                auto_verified=True,
                verification_source='Certification Authority Database',
                verification_confidence_score=88.0,
                verification_api_response=cert_data
            )
            self.stdout.write(f'Created specialty certification: {credential.license_number}')

    def load_pharmacy_licenses(self, base_dir, user):
        file_path = os.path.join(base_dir, 'pharmacy_licenses.json')
        if not os.path.exists(file_path):
            self.stdout.write(self.style.WARNING(f'Pharmacy licenses file not found: {file_path}'))
            return
        
        with open(file_path, 'r') as f:
            licenses = json.load(f)
        
        for license_data in licenses:
            credential = Credential.objects.create(
                user=user,
                credential_type='pharmacy_license',
                title=f"Pharmacy License - {license_data['current_position']}",
                license_number=license_data['license_number'],
                issuing_authority=f"{license_data['issuing_state']} Board of Pharmacy",
                issuing_state=license_data['issuing_state'],
                issue_date=datetime.strptime(license_data['issue_date'], '%Y-%m-%d').date(),
                expiry_date=datetime.strptime(license_data['expiry_date'], '%Y-%m-%d').date(),
                status='verified' if license_data['status'] == 'Active' else 'expired',
                notes=f"Pharmacist: {license_data['pharmacist_name']}\n"
                      f"Degree: {license_data['pharmacy_degree']}\n"
                      f"School: {license_data['graduating_school']}\n"
                      f"Current Position: {license_data['current_position']}\n"
                      f"Specialty Certification: {license_data['specialty_certification'] or 'None'}\n"
                      f"NABP e-Verify: {license_data['nabp_e_verification']}\n"
                      f"DEA Registration: {license_data['dea_registration']}\n"
                      f"Disciplinary Actions: {license_data['disciplinary_actions']}",
                auto_verified=True,
                verification_source='State Board of Pharmacy Database',
                verification_confidence_score=94.0,
                verification_api_response=license_data
            )
            self.stdout.write(f'Created pharmacy license: {credential.license_number}')
