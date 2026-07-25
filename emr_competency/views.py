from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import uuid
from .models import EMRSystem, CompetencyTest, CompetencyQuestion, CompetencyResult


@login_required
def emr_list(request):
    """List EMR/EHR systems"""
    systems = EMRSystem.objects.filter(is_active=True)
    tests = CompetencyTest.objects.filter(is_active=True)
    user_certs = CompetencyResult.objects.filter(user=request.user, certified=True)
    return render(request, 'emr_competency/emr_list.html', {
        'systems': systems,
        'tests': tests,
        'certifications': user_certs,
    })


@login_required
def competency_test(request, pk):
    """Take a competency test"""
    test = get_object_or_404(CompetencyTest, pk=pk, is_active=True)
    
    if CompetencyResult.objects.filter(user=request.user, test=test, certified=True).exists():
        messages.info(request, "You have already passed this competency test.")
        return redirect('emr:certification')

    questions = test.questions.all().order_by('?')[:test.total_questions]

    if request.method == 'POST':
        score = 0
        total = questions.count()
        for question in questions:
            user_answer = request.POST.get(f'question_{question.id}', '')
            if user_answer.upper().strip() == question.correct_answer.upper().strip():
                score += 1

        percentage = (score / max(total, 1)) * 100
        certified = percentage >= test.passing_score
        cert_number = f"EMR-{uuid.uuid4().hex[:8].upper()}" if certified else ''

        # Mock Detailed Analytics & AI Feedback
        skill_gaps = []
        if not certified:
            skill_gaps.append(f"Needs improvement in {test.get_standard_display()}")
        
        recommended_training = []
        if percentage < 80:
            recommended_training.append(f"Advanced {test.title} Workshop")

        CompetencyResult.objects.create(
            user=request.user,
            test=test,
            score=score,
            percentage=round(percentage, 1),
            certified=certified,
            certificate_number=cert_number,
            skill_gaps=skill_gaps,
            recommended_training=recommended_training,
            theoretical_score=percentage
        )

        if certified:
            messages.success(request, f'Congratulations! You are now certified! Certificate: {cert_number}')
        else:
            messages.warning(request, f'Score: {percentage:.0f}%. Need {test.passing_score}% to get certified.')

        return redirect('emr:certification')

    return render(request, 'emr_competency/competency_test.html', {
        'test': test,
        'questions': questions,
    })


@login_required
def certification(request):
    """View certifications"""
    results = CompetencyResult.objects.filter(user=request.user).select_related('test')
    certified = results.filter(certified=True)
    return render(request, 'emr_competency/certification.html', {
        'results': results,
        'certified': certified,
    })

@login_required
def simulation_dashboard(request):
    """Mock EMR/EHR Simulation Interface"""
    patients = [
        {"id": "PT-1049", "name": "Emily Chen", "age": 34, "condition": "Type 2 Diabetes", "status": "Stable"},
        {"id": "PT-2931", "name": "Marcus Johnson", "age": 58, "condition": "Hypertension", "status": "Critical Review"},
        {"id": "PT-8442", "name": "Sarah Williams", "age": 42, "condition": "Asthma", "status": "Follow-up"},
    ]
    return render(request, 'emr_competency/simulation.html', {'patients': patients})
