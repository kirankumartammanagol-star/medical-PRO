# HealthCareer Pro - Healthcare Job Portal & Assessment System

HealthCareer Pro is an advanced, AI-powered web platform designed specifically for the healthcare industry. It serves as a comprehensive ecosystem that bridges the gap between healthcare professionals and medical institutions by offering targeted job postings, clinical competency assessments, regulatory compliance training, and virtual patient simulation interviews.

## 🚀 Features

The platform is divided into several robust modules, each tailored to the rigorous demands of the healthcare sector:

### 1. Healthcare Skills Assessment Module
- **15 Specialized Categories:** Tests covering everything from *Patient Care Procedures* and *SNOMED CT Concepts* to *Medical Terminology*.
- **Anti-Cheat Engine:** Detects tab-switching and prevents page refreshes during assessments.
- **Dynamic Leaderboard:** Highlights top performers across different clinical disciplines.
- **Automated Certification:** Generates printable, high-quality certificates upon passing.

### 2. EMR / EHR Competency Module
- **10 Mock EHR Scenarios:** Tests evaluating proficiency in HL7 FHIR Fundamentals, ICD-10 Coding, and general Hospital Information Systems.
- **Simulation Dashboard:** An interactive mock workspace where candidates can view simulated patient rosters, check vital signs, and test API data retrievals.
- **Detailed AI Analytics:** Identifies specific skill gaps based on the user's performance and recommends targeted training.

### 3. Compliance & Regulatory Training Module
- **15 Mandatory Modules:** Comprehensive training covering HIPAA, OSHA Workplace Safety, Infection Prevention, Healthcare Cybersecurity, and more.
- **Embedded Training Content:** Each module includes simulated video lectures, learning objectives, and reading materials.
- **Strict Compliance Tracking:** Dashboards dynamically track the percentage of completed vs. pending mandatory training, generating compliance certificates upon completion.

### 4. Clinical Simulation Interview System
- **12 Virtual Patient Cases:** Scenarios spanning Trauma Management, Pediatric Emergencies, Cardiac Emergencies, and Diagnostic workflows.
- **Interactive Decision Making:** Candidates navigate a series of clinical steps (analyzing history, reviewing symptoms, picking treatments) against a strict time limit.
- **Hiring Recommendations:** AI evaluates clinical reasoning and outputs a hiring recommendation (e.g., *Highly Recommended, Conditional*) based on patient outcomes and critical steps taken.

### 5. Advanced Job Board & Authentication
- **Healthcare-Specific Postings:** Filter jobs by clinical specialty, location, and required certifications.
- **JWT & REST APIs:** Complete API backend (`/api/v1/...`) ready to serve mobile applications or decouple the frontend.

## 🛠 Tech Stack

- **Backend Framework:** Django (Python)
- **Database:** SQLite (Development) / PostgreSQL (Production ready)
- **Frontend UI/UX:** Vanilla HTML/CSS/JS with modern glassmorphism, responsive grid layouts, and dynamic micro-animations.
- **Authentication:** Django Authentication & custom JWT for REST APIs.

## ⚙️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd "Health care"
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Seed the Database (Crucial for Demo/Testing):**
   Run the following management commands to instantly populate the platform with realistic medical data, test questions, and virtual patients:
   ```bash
   python manage.py seed_assessments
   python manage.py seed_emr
   python manage.py seed_compliance
   python manage.py seed_simulations
   ```

6. **Start the Development Server:**
   ```bash
   python manage.py runserver
   ```
   Navigate to `http://127.0.0.1:8000/` in your browser to access the portal.

## 📁 Project Structure Highlights

- `/assessments/`: Handles generic healthcare skill tests.
- `/emr_competency/`: Manages EHR/HL7 FHIR mock tests and simulation interfaces.
- `/compliance/`: Handles HIPAA/OSHA regulatory training, learning materials, and quizzes.
- `/simulations/`: Powers the virtual patient case studies and interview evaluation system.
- `/core/`: Central app managing global API views, common logic, and user routing.
- `/templates/`: All HTML templates, structured by app for modularity.
- `/static/`: CSS and JavaScript files controlling the responsive, modern UI.

## 📜 License
This project is proprietary and built specifically for the HealthCareer Pro ecosystem. All rights reserved.
