from django.core.management.base import BaseCommand
from assessments.models import Assessment, Question
import random

class Command(BaseCommand):
    help = 'Seeds the database with 15 Healthcare Assessments and 10 questions each'

    def handle(self, *args, **kwargs):
        categories = [
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

        difficulties = ['beginner', 'intermediate', 'advanced']

        self.stdout.write('Clearing old assessments...')
        Assessment.objects.all().delete()

        self.stdout.write('Generating 15 Assessments...')

        for cat_id, cat_name in categories:
            diff = random.choice(difficulties)
            assessment = Assessment.objects.create(
                title=f"{cat_name} Certification Exam",
                description=f"Comprehensive assessment testing your knowledge in {cat_name}. Contains multiple choice questions requiring a deep understanding of standard practices and clinical standards.",
                category=cat_id,
                difficulty=diff,
                time_limit_minutes=30,
                passing_score=70,
                total_questions=10,
                is_active=True,
                clinical_domain='General Medicine',
            )

            # Generate 10 questions for each
            for i in range(1, 11):
                options = [
                    f"Appropriate clinical procedure variant {random.randint(1, 100)}",
                    f"Standard protocol application {random.randint(1, 100)}",
                    f"Incorrect interpretation {random.randint(1, 100)}",
                    f"Alternative standard {random.randint(1, 100)}"
                ]
                random.shuffle(options)
                correct_ans = options[0]

                Question.objects.create(
                    assessment=assessment,
                    text=f"Which of the following best describes the core principle of {cat_name} in scenario {i}?",
                    question_type='mcq',
                    option_a=options[0],
                    option_b=options[1],
                    option_c=options[2],
                    option_d=options[3],
                    correct_answer=correct_ans,
                    explanation=f"This is the standard accepted practice according to {cat_name} guidelines.",
                    points=10,
                    order=i,
                )

        self.stdout.write(self.style.SUCCESS('Successfully seeded 15 assessments with 10 questions each.'))
