from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
import json
import base64
import hmac
import hashlib
from datetime import datetime, timedelta
from django.conf import settings
from .models import UserProfile, Hospital, MedicalCollege
from credentials.models import Credential
from jobs.models import JobListing
from assessments.models import Assessment
from emr_competency.models import CompetencyTest
from compliance.models import ComplianceModule
from simulations.models import Simulation

# Simple JWT implementation for the requirement
def generate_jwt(user):
    header = base64.urlsafe_b64encode(json.dumps({"alg": "HS256", "typ": "JWT"}).encode()).decode().rstrip('=')
    payload_data = {
        "user_id": user.id,
        "username": user.username,
        "exp": (datetime.utcnow() + timedelta(hours=24)).timestamp()
    }
    payload = base64.urlsafe_b64encode(json.dumps(payload_data).encode()).decode().rstrip('=')
    signature = base64.urlsafe_b64encode(
        hmac.new(settings.SECRET_KEY.encode(), f"{header}.{payload}".encode(), hashlib.sha256).digest()
    ).decode().rstrip('=')
    return f"{header}.{payload}.{signature}"

def verify_jwt(token):
    try:
        parts = token.split('.')
        if len(parts) != 3: return None
        header, payload, signature = parts
        expected_sig = base64.urlsafe_b64encode(
            hmac.new(settings.SECRET_KEY.encode(), f"{header}.{payload}".encode(), hashlib.sha256).digest()
        ).decode().rstrip('=')
        if signature != expected_sig: return None
        payload_data = json.loads(base64.urlsafe_b64decode(payload + '==').decode())
        if payload_data.get('exp', 0) < datetime.utcnow().timestamp(): return None
        return User.objects.get(id=payload_data['user_id'])
    except Exception:
        return None

def jwt_required(view_func):
    def wrapped(request, *args, **kwargs):
        auth_header = request.headers.get('Authorization', '')
        if not auth_header.startswith('Bearer '):
            return JsonResponse({'error': 'Unauthorized, missing JWT'}, status=401)
        token = auth_header.split(' ')[1]
        user = verify_jwt(token)
        if not user:
            return JsonResponse({'error': 'Unauthorized, invalid or expired JWT'}, status=401)
        request.user = user
        return view_func(request, *args, **kwargs)
    return wrapped

@csrf_exempt
def api_login(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user = authenticate(username=data.get('username'), password=data.get('password'))
            if user:
                token = generate_jwt(user)
                return JsonResponse({'token': token})
            return JsonResponse({'error': 'Invalid credentials'}, status=401)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    return JsonResponse({'error': 'Method not allowed'}, status=405)

@jwt_required
def api_profile(request):
    try:
        profile = request.user.profile
        data = {
            'username': request.user.username,
            'email': request.user.email,
            'role': profile.get_role_display(),
            'specialization': profile.specialization,
            'experience_years': profile.experience_years
        }
        return JsonResponse({'profile': data})
    except UserProfile.DoesNotExist:
        return JsonResponse({'error': 'Profile not found'}, status=404)

@jwt_required
def api_jobs(request):
    jobs = JobListing.objects.filter(is_active=True).values(
        'id', 'title', 'hospital_name', 'specialty', 'job_type', 'location', 'posted_date'
    )
    return JsonResponse({'jobs': list(jobs)})

@jwt_required
def api_credentials(request):
    creds = Credential.objects.filter(user=request.user).values(
        'id', 'credential_type', 'title', 'status', 'issuing_authority', 'issue_date', 'expiry_date'
    )
    return JsonResponse({'credentials': list(creds)})

@jwt_required
def api_assessments(request):
    assessments = Assessment.objects.filter(is_active=True).values(
        'id', 'title', 'category', 'difficulty', 'total_questions', 'passing_score'
    )
    return JsonResponse({'assessments': list(assessments)})

@jwt_required
def api_emr_tests(request):
    emr_tests = CompetencyTest.objects.filter(is_active=True).values(
        'id', 'title', 'standard', 'skill_level', 'total_questions', 'passing_score'
    )
    return JsonResponse({'emr_tests': list(emr_tests)})

@jwt_required
def api_compliance(request):
    modules = ComplianceModule.objects.filter(is_mandatory=True).values(
        'id', 'title', 'regulation', 'duration_minutes', 'required_score'
    )
    return JsonResponse({'compliance_modules': list(modules)})

@jwt_required
def api_simulations(request):
    simulations = Simulation.objects.filter(is_active=True).values(
        'id', 'title', 'scenario_type', 'difficulty', 'time_limit_minutes', 'patient_name'
    )
    return JsonResponse({'simulations': list(simulations)})
