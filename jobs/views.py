from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import JobListing, Application, Partnership


@login_required
def job_list(request):
    """List all active job listings with filters"""
    jobs = JobListing.objects.filter(is_active=True)

    # Filters
    specialty = request.GET.get('specialty', '')
    job_type = request.GET.get('job_type', '')
    location = request.GET.get('location', '')
    experience = request.GET.get('experience', '')

    if specialty:
        jobs = jobs.filter(specialty=specialty)
    if job_type:
        jobs = jobs.filter(job_type=job_type)
    if location:
        jobs = jobs.filter(location__icontains=location)
    if experience:
        jobs = jobs.filter(experience_level=experience)

    # If no jobs exist, provide sample data
    if not jobs.exists():
        sample_jobs = [
            {'title': 'Senior Cardiologist', 'hospital_name': 'Apollo Hospital, Bangalore', 'specialty': 'Cardiology', 'job_type': 'Full Time', 'location': 'Bangalore, Karnataka', 'salary_range': '₹25,00,000 - ₹40,00,000', 'experience_level': 'Senior Level', 'is_urgent': True, 'posted_date': '2 days ago'},
            {'title': 'Staff Nurse - ICU', 'hospital_name': 'Fortis Healthcare, Delhi', 'specialty': 'Nursing', 'job_type': 'Full Time', 'location': 'New Delhi', 'salary_range': '₹4,50,000 - ₹7,00,000', 'experience_level': 'Mid Level', 'is_urgent': False, 'posted_date': '5 days ago'},
            {'title': 'Emergency Medicine Physician', 'hospital_name': 'AIIMS, New Delhi', 'specialty': 'Emergency Medicine', 'job_type': 'Full Time', 'location': 'New Delhi', 'salary_range': '₹15,00,000 - ₹25,00,000', 'experience_level': 'Senior Level', 'is_urgent': True, 'posted_date': '1 day ago'},
            {'title': 'Pediatrics Resident', 'hospital_name': 'Manipal Hospital, Bangalore', 'specialty': 'Pediatrics', 'job_type': 'Residency', 'location': 'Bangalore, Karnataka', 'salary_range': '₹8,00,000 - ₹12,00,000', 'experience_level': 'Entry Level', 'is_urgent': False, 'posted_date': '1 week ago'},
            {'title': 'Lab Technician', 'hospital_name': 'Max Healthcare, Mumbai', 'specialty': 'Lab Technician', 'job_type': 'Full Time', 'location': 'Mumbai, Maharashtra', 'salary_range': '₹3,50,000 - ₹5,00,000', 'experience_level': 'Entry Level', 'is_urgent': False, 'posted_date': '3 days ago'},
            {'title': 'Neurosurgeon', 'hospital_name': 'Medanta Hospital, Gurugram', 'specialty': 'Neurology', 'job_type': 'Full Time', 'location': 'Gurugram, Haryana', 'salary_range': '₹35,00,000 - ₹60,00,000', 'experience_level': 'Expert Level', 'is_urgent': True, 'posted_date': '4 days ago'},
            {'title': 'Clinical Pharmacist', 'hospital_name': 'Narayana Health, Bangalore', 'specialty': 'Pharmacy', 'job_type': 'Full Time', 'location': 'Bangalore, Karnataka', 'salary_range': '₹5,00,000 - ₹8,00,000', 'experience_level': 'Mid Level', 'is_urgent': False, 'posted_date': '6 days ago'},
            {'title': 'Oncology Fellow', 'hospital_name': 'Tata Memorial Hospital, Mumbai', 'specialty': 'Oncology', 'job_type': 'Fellowship', 'location': 'Mumbai, Maharashtra', 'salary_range': '₹12,00,000 - ₹18,00,000', 'experience_level': 'Mid Level', 'is_urgent': False, 'posted_date': '2 weeks ago'},
        ]
    else:
        sample_jobs = None

    specialties = JobListing.SPECIALTY_CHOICES
    job_types = JobListing.JOB_TYPES
    experience_levels = JobListing.EXPERIENCE_LEVELS

    return render(request, 'jobs/job_list.html', {
        'jobs': jobs,
        'sample_jobs': sample_jobs,
        'specialties': specialties,
        'job_types': job_types,
        'experience_levels': experience_levels,
        'selected_specialty': specialty,
        'selected_type': job_type,
        'selected_location': location,
        'selected_experience': experience,
    })


@login_required
def job_detail(request, pk):
    """View job listing details"""
    job = get_object_or_404(JobListing, pk=pk)
    job.views_count += 1
    job.save()
    has_applied = Application.objects.filter(job=job, candidate=request.user).exists()
    return render(request, 'jobs/job_detail.html', {
        'job': job,
        'has_applied': has_applied,
    })


@login_required
def apply_job(request, pk):
    """Apply for a job"""
    job = get_object_or_404(JobListing, pk=pk)

    if Application.objects.filter(job=job, candidate=request.user).exists():
        messages.warning(request, 'You have already applied for this position.')
        return redirect('jobs:job_detail', pk=pk)

    if request.method == 'POST':
        application = Application.objects.create(
            job=job,
            candidate=request.user,
            cover_letter=request.POST.get('cover_letter', ''),
        )
        if request.FILES.get('resume'):
            application.resume = request.FILES['resume']
            application.save()

        messages.success(request, 'Application submitted successfully!')
        return redirect('jobs:my_applications')

    return render(request, 'jobs/apply.html', {'job': job})


@login_required
def my_applications(request):
    """View user's applications"""
    applications = Application.objects.filter(candidate=request.user).select_related('job')
    return render(request, 'jobs/my_applications.html', {'applications': applications})


@login_required
def partnerships(request):
    """Hospital-Education integration partnerships"""
    all_partnerships = Partnership.objects.filter(is_active=True)

    # Sample data if no partnerships
    if not all_partnerships.exists():
        sample_partnerships = [
            {'hospital_name': 'Apollo Hospital', 'college_name': 'KLE Medical College', 'program_type': 'Clinical Rotation', 'students_enrolled': 120, 'placement_rate': 85.5, 'start_date': '2025-01-15'},
            {'hospital_name': 'AIIMS New Delhi', 'college_name': 'JIPMER Puducherry', 'program_type': 'Research Collaboration', 'students_enrolled': 45, 'placement_rate': 92.0, 'start_date': '2024-06-01'},
            {'hospital_name': 'Fortis Healthcare', 'college_name': 'Manipal Academy of Higher Education', 'program_type': 'Internship Program', 'students_enrolled': 200, 'placement_rate': 78.3, 'start_date': '2025-03-01'},
            {'hospital_name': 'Narayana Health', 'college_name': 'St. Johns Medical College', 'program_type': 'Residency Program', 'students_enrolled': 60, 'placement_rate': 95.0, 'start_date': '2024-09-01'},
            {'hospital_name': 'Max Healthcare', 'college_name': 'Armed Forces Medical College', 'program_type': 'Fellowship Program', 'students_enrolled': 30, 'placement_rate': 88.0, 'start_date': '2025-02-01'},
            {'hospital_name': 'Medanta Hospital', 'college_name': 'CMC Vellore', 'program_type': 'Direct Recruitment Pipeline', 'students_enrolled': 90, 'placement_rate': 91.5, 'start_date': '2024-12-01'},
        ]
    else:
        sample_partnerships = None

    stats = {
        'total_partnerships': all_partnerships.count() or 6,
        'total_students': sum(p.students_enrolled for p in all_partnerships) or 545,
        'avg_placement': 88.4,
    }

    return render(request, 'jobs/partnerships.html', {
        'partnerships': all_partnerships,
        'sample_partnerships': sample_partnerships,
        'stats': stats,
    })
