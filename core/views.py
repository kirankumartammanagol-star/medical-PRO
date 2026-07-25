from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import UserProfile, Hospital, MedicalCollege, ContactMessage
from credentials.models import Credential
from assessments.models import AssessmentResult
from compliance.models import ComplianceRecord
from jobs.models import JobListing


def index(request):
    """Landing page"""
    stats = {
        'total_hospitals': Hospital.objects.count() or 150,
        'total_jobs': JobListing.objects.count() or 1200,
        'total_professionals': UserProfile.objects.count() or 5000,
        'total_colleges': MedicalCollege.objects.count() or 75,
    }
    features = [
        {
            'icon': 'fa-certificate',
            'title': 'Clinical Credential Verification',
            'description': 'Automatic verification of professional licenses and certifications with integration to healthcare certification databases.',
            'color': '#00d4aa',
        },
        {
            'icon': 'fa-stethoscope',
            'title': 'Clinical Skill Assessment',
            'description': 'Comprehensive assessments covering patient care, medical coding (ICD-10), clinical decision-making, and SNOMED CT standards.',
            'color': '#667eea',
        },
        {
            'icon': 'fa-laptop-medical',
            'title': 'EMR/EHR Competency Testing',
            'description': 'Evaluate proficiency in Electronic Medical Records systems and HL7 FHIR interoperability standards.',
            'color': '#f093fb',
        },
        {
            'icon': 'fa-shield-alt',
            'title': 'Compliance & Regulatory Training',
            'description': 'HIPAA compliance modules, privacy awareness assessments, and regulatory knowledge evaluation.',
            'color': '#4facfe',
        },
        {
            'icon': 'fa-user-md',
            'title': 'Clinical Simulation Interviews',
            'description': 'Virtual patient simulations and case-based clinical interview preparation with real-time feedback.',
            'color': '#43e97b',
        },
        {
            'icon': 'fa-chart-line',
            'title': 'Workforce Demand Forecasting',
            'description': 'AI-powered analysis of healthcare workforce demand with specialty shortage predictions.',
            'color': '#fa709a',
        },
    ]
    return render(request, 'core/index.html', {'stats': stats, 'features': features})


def about(request):
    """About page"""
    return render(request, 'core/about.html')


def contact(request):
    """Contact page"""
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message_text = request.POST.get('message')
        ContactMessage.objects.create(name=name, email=email, subject=subject, message=message_text)
        messages.success(request, 'Your message has been sent successfully!')
        return redirect('contact')
    return render(request, 'core/contact.html')


@login_required
def dashboard(request):
    """Dashboard page"""
    context = {
        'credentials_count': Credential.objects.filter(user=request.user).count(),
        'assessments_count': AssessmentResult.objects.filter(user=request.user).count(),
        'compliance_count': ComplianceRecord.objects.filter(user=request.user, passed=True).count(),
        'recent_jobs': JobListing.objects.filter(is_active=True).order_by('-posted_date')[:5],
    }
    return render(request, 'core/dashboard.html', context)


def register_view(request):
    """User registration"""
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        role = request.POST.get('role', 'doctor')

        if password != password2:
            messages.error(request, 'Passwords do not match!')
            return render(request, 'core/register.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists!')
            return render(request, 'core/register.html')

        user = User.objects.create_user(
            username=username, email=email, password=password,
            first_name=first_name, last_name=last_name
        )
        UserProfile.objects.create(user=user, role=role)
        login(request, user)
        messages.success(request, 'Registration successful! Welcome to HealthCareer Pro.')
        return redirect('dashboard')

    return render(request, 'core/register.html')


def login_view(request):
    """User login"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {user.first_name}!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password!')

    return render(request, 'core/login.html')


def logout_view(request):
    """User logout"""
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('index')
