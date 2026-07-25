from django.core.management.base import BaseCommand
from simulations.models import Simulation, SimulationStep
import random

class Command(BaseCommand):
    help = 'Seeds the database with 12 Clinical Simulation Scenarios and steps'

    def handle(self, *args, **kwargs):
        categories = [
            ("Emergency Response", "emergency"),
            ("Diagnostic Scenario", "diagnosis"),
            ("Patient Care Management", "patient_care"),
            ("Surgical Decision Making", "surgical"),
            ("Medication Management", "medication"),
            ("Triage Assessment", "triage"),
            ("Patient Communication", "communication"),
            ("Ethical Dilemma", "ethics"),
            ("Critical Care Management", "critical_care"),
            ("Pediatric Emergency", "pediatric"),
            ("Cardiac Emergency", "cardiac"),
            ("Trauma Management", "trauma"),
        ]

        self.stdout.write('Clearing old simulations...')
        Simulation.objects.all().delete()

        self.stdout.write('Generating 12 Clinical Simulations...')

        for idx, (title, cat_id) in enumerate(categories):
            sim = Simulation.objects.create(
                title=f"{title} - Virtual Patient Case",
                scenario_type=cat_id,
                difficulty=random.choice(['beginner', 'intermediate', 'advanced']),
                description=f"A comprehensive {title.lower()} simulation designed to test your clinical reasoning, decision-making, and patient care workflows.",
                patient_name=f"Patient {idx+1}",
                patient_age=random.randint(5, 85),
                patient_gender=random.choice(["Male", "Female"]),
                patient_history="Hypertension, Type 2 Diabetes" if idx % 2 == 0 else "No significant past medical history.",
                presenting_symptoms=f"The patient presents with severe symptoms related to {title.lower()}.",
                vital_signs='{"HR": 110, "BP": "140/90", "Temp": 38.5}',
                correct_diagnosis=f"Condition requiring {title.lower()} protocols.",
                expected_actions="1. Initial Assessment\n2. Stabilize Patient\n3. Order Labs\n4. Administer Meds",
                time_limit_minutes=30,
                is_active=True,
                patient_complaint="Doctor, I feel terrible. It started a few hours ago...",
                medical_history="See patient chart for details.",
                red_flags="Watch out for sudden deterioration.",
                educational_objectives="Identify critical signs, execute correct workflow."
            )

            # Generate 5 interactive steps for each simulation
            for step_num in range(1, 6):
                options = [
                    "A. Administer standard protocol treatment immediately.",
                    "B. Wait for further lab results before acting.",
                    "C. Consult with a specialist.",
                    "D. Discharge the patient with advice."
                ]
                random.shuffle(options)
                
                SimulationStep.objects.create(
                    simulation=sim,
                    step_number=step_num,
                    description=f"Phase {step_num}: Patient condition updates. You must decide the next clinical action.",
                    question=f"Based on the {title} protocols, what is your next immediate step?",
                    option_a=options[0],
                    option_b=options[1],
                    option_c=options[2],
                    option_d=options[3],
                    correct_option="A",  # Dummy seeding logic
                    feedback_correct="Excellent clinical judgment. This stabilizes the patient.",
                    feedback_incorrect="Incorrect. This action may compromise patient safety or delay necessary treatment.",
                    step_type='assessment',
                    time_limit_seconds=60,
                    clinical_reasoning="Early intervention improves patient outcomes.",
                    common_errors="Delaying treatment while waiting for non-critical labs."
                )

        self.stdout.write(self.style.SUCCESS('Successfully seeded 12 Clinical Simulations with interactive steps.'))
