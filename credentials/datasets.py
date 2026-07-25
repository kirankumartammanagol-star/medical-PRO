import json
from datetime import date, timedelta
import random

def generate_medical_licenses():
    """Generate realistic medical license dataset"""
    licenses = []
    states = ['California', 'New York', 'Texas', 'Florida', 'Illinois', 'Pennsylvania', 'Ohio', 'Georgia', 'North Carolina', 'Michigan']
    specialties = ['Family Medicine', 'Internal Medicine', 'Pediatrics', 'Surgery', 'Obstetrics & Gynecology', 'Psychiatry', 'Anesthesiology', 'Radiology', 'Dermatology', 'Cardiology']
    
    for i in range(100):
        license_data = {
            "license_number": f"MD{random.randint(10000, 99999)}-{random.choice(states)[:2].upper()}",
            "physician_name": f"Dr. {random.choice(['John', 'Jane', 'Michael', 'Sarah', 'Robert', 'Emily', 'David', 'Lisa'])} {random.choice(['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis'])}",
            "issuing_state": random.choice(states),
            "issue_date": date(2020 + random.randint(0, 5), random.randint(1, 12), random.randint(1, 28)).isoformat(),
            "expiry_date": date(2025 + random.randint(0, 3), random.randint(1, 12), random.randint(1, 28)).isoformat(),
            "status": random.choice(['Active', 'Active', 'Active', 'Suspended', 'Expired']),
            "specialty": random.choice(specialties),
            "board_certified": random.choice([True, False, True, True]),
            "disciplinary_actions": random.choice([False, False, False, True]),
            "malpractice_claims": random.randint(0, 5),
            "license_type": random.choice(['MD', 'DO']),
            "dea_registration": f"AB{random.randint(1000000, 9999999)}",
            "npi_number": f"{random.randint(1000000000, 9999999999)}"
        }
        licenses.append(license_data)
    
    return licenses

def generate_nursing_licenses():
    """Generate realistic nursing license dataset"""
    licenses = []
    states = ['California', 'New York', 'Texas', 'Florida', 'Illinois', 'Pennsylvania', 'Ohio', 'Georgia', 'North Carolina', 'Michigan']
    license_types = ['RN', 'LPN', 'APRN', 'CNS', 'CNM', 'CRNA']
    specialties = ['Medical-Surgical', 'ICU', 'Emergency', 'Pediatrics', 'OB/GYN', 'Psychiatric', 'Oncology', 'Surgical', 'Cardiac', 'Neurology']
    
    for i in range(150):
        license_data = {
            "license_number": f"{random.choice(['RN', 'LPN', 'APRN'])}{random.randint(100000, 999999)}-{random.choice(states)[:2].upper()}",
            "nurse_name": f"{random.choice(['Mary', 'Patricia', 'Jennifer', 'Linda', 'Elizabeth', 'Barbara', 'Susan', 'Jessica'])} {random.choice(['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis'])}",
            "issuing_state": random.choice(states),
            "license_type": random.choice(license_types),
            "issue_date": date(2018 + random.randint(0, 7), random.randint(1, 12), random.randint(1, 28)).isoformat(),
            "expiry_date": date(2024 + random.randint(0, 3), random.randint(1, 12), random.randint(1, 28)).isoformat(),
            "status": random.choice(['Active', 'Active', 'Active', 'Delinquent', 'Suspended', 'Expired']),
            "specialty": random.choice(specialties),
            "advanced_certification": random.choice([True, False, True, False, True]),
            "bls_certified": True,
            "acls_certified": random.choice([True, False, True, True]),
            "years_experience": random.randint(1, 30),
            "current_employer": random.choice(['General Hospital', 'Medical Center', 'Community Clinic', 'Specialty Hospital', 'Rehabilitation Center']),
            "disciplinary_actions": random.choice([False, False, False, False, True])
        }
        licenses.append(license_data)
    
    return licenses

def generate_board_certifications():
    """Generate realistic board certification dataset"""
    certifications = []
    boards = ['American Board of Internal Medicine', 'American Board of Surgery', 'American Board of Pediatrics', 'American Board of Family Medicine', 
              'American Board of Anesthesiology', 'American Board of Psychiatry', 'American Board of Radiology', 'American Board of Dermatology',
              'American Board of Obstetrics & Gynecology', 'American Board of Neurology']
    
    subspecialties = {
        'American Board of Internal Medicine': ['Cardiovascular Disease', 'Gastroenterology', 'Pulmonary Disease', 'Nephrology', 'Endocrinology', 'Hematology', 'Infectious Disease'],
        'American Board of Surgery': ['Surgical Critical Care', 'Vascular Surgery', 'Pediatric Surgery', 'Surgical Oncology', 'Thoracic Surgery'],
        'American Board of Pediatrics': ['Neonatal-Perinatal Medicine', 'Pediatric Cardiology', 'Pediatric Critical Care', 'Pediatric Emergency Medicine'],
        'American Board of Family Medicine': ['Geriatric Medicine', 'Sports Medicine', 'Hospice & Palliative Medicine', 'Adolescent Medicine'],
        'American Board of Anesthesiology': ['Critical Care Medicine', 'Pain Medicine', 'Cardiothoracic Anesthesiology'],
        'American Board of Psychiatry': ['Child & Adolescent Psychiatry', 'Geriatric Psychiatry', 'Addiction Psychiatry', 'Forensic Psychiatry'],
        'American Board of Radiology': ['Interventional Radiology', 'Neuroradiology', 'Nuclear Radiology', 'Pediatric Radiology'],
        'American Board of Dermatology': ['Dermatopathology', 'Pediatric Dermatology', 'Mohs Surgery'],
        'American Board of Obstetrics & Gynecology': ['Maternal-Fetal Medicine', 'Reproductive Endocrinology', 'Gynecologic Oncology'],
        'American Board of Neurology': ['Vascular Neurology', 'Epilepsy', 'Neuromuscular Medicine', 'Movement Disorders']
    }
    
    for i in range(80):
        board = random.choice(boards)
        subspecialty = random.choice(subspecialties.get(board, ['General'])) if random.choice([True, False]) else None
        
        cert_data = {
            "certification_id": f"CERT-{random.randint(100000, 999999)}",
            "physician_name": f"Dr. {random.choice(['William', 'Richard', 'Joseph', 'Thomas', 'Charles', 'Christopher', 'Daniel', 'Matthew'])} {random.choice(['Anderson', 'Thomas', 'Taylor', 'Moore', 'Jackson', 'Martin', 'Lee', 'Thompson'])}",
            "board_name": board,
            "specialty": random.choice(['Internal Medicine', 'Surgery', 'Pediatrics', 'Family Medicine', 'Anesthesiology', 'Psychiatry', 'Radiology', 'Dermatology', 'OB/GYN', 'Neurology']),
            "subspecialty": subspecialty,
            "certification_date": date(2015 + random.randint(0, 8), random.randint(1, 12), random.randint(1, 28)).isoformat(),
            "expiry_date": date(2025 + random.randint(0, 5), random.randint(1, 12), random.randint(1, 28)).isoformat(),
            "status": random.choice(['Certified', 'Certified', 'Certified', 'Expired', 'Revoked']),
            "maintenance_of_certification": random.choice([True, True, False]),
            "last_moc_date": date(2020 + random.randint(0, 4), random.randint(1, 12), random.randint(1, 28)).isoformat() if random.choice([True, False]) else None,
            "cme_credits_earned": random.randint(50, 200),
            "practice_address": f"{random.randint(100, 9999)} {random.choice(['Main', 'Oak', 'Maple', 'Cedar', 'Elm'])} St, {random.choice(['Springfield', 'Riverside', 'Franklin', 'Georgetown', 'Madison'])}, {random.choice(states)} {random.randint(10000, 99999)}"
        }
        certifications.append(cert_data)
    
    return certifications

def generate_specialty_certifications():
    """Generate specialty healthcare certifications"""
    certifications = []
    cert_types = [
        'ACLS', 'BLS', 'PALS', 'NRP', 'TNCC', 'ENPC', 'CEN', 'CCRN', 'CWCN', 'CNOR',
        'CPhT', 'CPhT-Adv', 'RRT', 'CRT', 'RDCS', 'RDMS', 'CMT', 'CMA', 'RMA', 'NCLEX',
        'CNS', 'CNSC', 'OCN', 'CPHQ', 'RHIA', 'RHIT', 'CCS', 'CPC', 'COC', 'CRC'
    ]
    
    issuing_orgs = [
        'American Heart Association', 'American Nurses Credentialing Center', 'National Board for Respiratory Care',
        'American Registry for Diagnostic Medical Sonography', 'American Medical Technologists',
        'American Association of Medical Assistants', 'National Healthcareer Association',
        'American Health Information Management Association', 'American Academy of Professional Coders'
    ]
    
    for i in range(120):
        cert_data = {
            "certification_id": f"{random.choice(cert_types)}-{random.randint(100000, 999999)}",
            "holder_name": f"{random.choice(['James', 'Robert', 'Michael', 'William', 'David', 'Richard', 'Joseph', 'Thomas'])} {random.choice(['Wilson', 'Moore', 'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White', 'Harris'])}",
            "certification_type": random.choice(cert_types),
            "issuing_organization": random.choice(issuing_orgs),
            "issue_date": date(2019 + random.randint(0, 5), random.randint(1, 12), random.randint(1, 28)).isoformat(),
            "expiry_date": date(2024 + random.randint(0, 3), random.randint(1, 12), random.randint(1, 28)).isoformat(),
            "status": random.choice(['Active', 'Active', 'Active', 'Expired', 'Suspended']),
            "renewal_required": True,
            "continuing_education_required": random.choice([True, False]),
            "practice_area": random.choice(['Emergency Medicine', 'Critical Care', 'Surgery', 'Pediatrics', 'Cardiology', 'Radiology', 'Laboratory', 'Pharmacy']),
            "verification_code": f"VERIFY-{random.randint(100000, 999999)}"
        }
        certifications.append(cert_data)
    
    return certifications

def generate_pharmacy_licenses():
    """Generate pharmacy license dataset"""
    licenses = []
    states = ['California', 'New York', 'Texas', 'Florida', 'Illinois', 'Pennsylvania', 'Ohio', 'Georgia', 'North Carolina', 'Michigan']
    
    for i in range(60):
        license_data = {
            "license_number": f"RPH{random.randint(10000, 99999)}-{random.choice(states)[:2].upper()}",
            "pharmacist_name": f"{random.choice(['Jennifer', 'Amanda', 'Michelle', 'Kimberly', 'Ashley', 'Stephanie', 'Rebecca', 'Laura'])} {random.choice(['Martinez', 'Robinson', 'Clark', 'Rodriguez', 'Lewis', 'Lee', 'Walker', 'Hall'])}",
            "issuing_state": random.choice(states),
            "issue_date": date(2016 + random.randint(0, 8), random.randint(1, 12), random.randint(1, 28)).isoformat(),
            "expiry_date": date(2024 + random.randint(0, 2), random.randint(1, 12), random.randint(1, 28)).isoformat(),
            "status": random.choice(['Active', 'Active', 'Active', 'Probation', 'Suspended', 'Expired']),
            "pharmacy_degree": random.choice(['PharmD', 'PharmD', 'PharmD', 'BS Pharmacy']),
            "graduating_school": random.choice(['University of Texas', 'Purdue University', 'University of Michigan', 'University of California', 'Ohio State University', 'University of Florida']),
            "nabp_e_verification": f"e-Verify-{random.randint(100000, 999999)}",
            "dea_registration": f"BX{random.randint(1000000, 9999999)}",
            "current_position": random.choice(['Staff Pharmacist', 'Clinical Pharmacist', 'Pharmacy Manager', 'Director of Pharmacy', 'Compounding Pharmacist']),
            "specialty_certification": random.choice([None, 'BCPS', 'BCGP', 'BCPP', 'BCCP', 'BCNSP']),
            "disciplinary_actions": random.choice([False, False, False, False, True])
        }
        licenses.append(license_data)
    
    return licenses

# Generate all datasets
if __name__ == "__main__":
    datasets = {
        "medical_licenses": generate_medical_licenses(),
        "nursing_licenses": generate_nursing_licenses(),
        "board_certifications": generate_board_certifications(),
        "specialty_certifications": generate_specialty_certifications(),
        "pharmacy_licenses": generate_pharmacy_licenses()
    }
    
    # Save to JSON files
    for dataset_name, data in datasets.items():
        with open(f"{dataset_name}.json", "w") as f:
            json.dump(data, f, indent=2)
        print(f"Generated {len(data)} records for {dataset_name}")
    
    print("\nAll credential verification datasets generated successfully!")
