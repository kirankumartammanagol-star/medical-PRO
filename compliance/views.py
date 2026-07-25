from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import uuid
from .models import ComplianceModule, ComplianceQuiz, ComplianceRecord


@login_required
def module_list(request):
    """List all compliance training modules"""
    modules = ComplianceModule.objects.all()
    completed = ComplianceRecord.objects.filter(user=request.user, passed=True).values_list('module_id', flat=True)
    stats = {
        'total_modules': modules.count(),
        'completed': len(completed),
        'mandatory': modules.filter(is_mandatory=True).count(),
    }
    return render(request, 'compliance/module_list.html', {
        'modules': modules,
        'completed_ids': list(completed),
        'stats': stats,
    })


@login_required
def training_module(request, pk):
    """View training module and take quiz"""
    module = get_object_or_404(ComplianceModule, pk=pk)
    
    if ComplianceRecord.objects.filter(user=request.user, module=module, passed=True).exists():
        messages.info(request, "You have already completed this compliance training.")
        return redirect('compliance:compliance_dashboard')
        
    questions = module.quizzes.all().order_by('?')[:15]

    if request.method == 'POST':
        score = 0
        total = questions.count()
        for question in questions:
            user_answer = request.POST.get(f'question_{question.id}', '')
            if user_answer.upper() == question.correct_answer.upper():
                score += 1

        percentage = (score / max(total, 1)) * 100
        passed = percentage >= module.required_score
        cert_id = f"COMP-{uuid.uuid4().hex[:8].upper()}" if passed else ''

        weak_areas = []
        if not passed:
            weak_areas.append(f"Review core concepts of {module.get_regulation_display()}")
        elif percentage < 90:
            weak_areas.append("Minor knowledge gaps in edge cases")
            
        ComplianceRecord.objects.create(
            user=request.user,
            module=module,
            score=score,
            percentage=round(percentage, 1),
            passed=passed,
            certificate_id=cert_id,
            weak_areas=weak_areas,
            remediation_required=not passed
        )

        if passed:
            messages.success(request, f'Module completed! Score: {percentage:.0f}%. Certificate: {cert_id}')
        else:
            messages.warning(request, f'Score: {percentage:.0f}%. Required: {module.required_score}%. Please retry.')

        return redirect('compliance:compliance_dashboard')

    return render(request, 'compliance/training_module.html', {
        'module': module,
        'questions': questions,
    })


@login_required
def compliance_dashboard(request):
    """Compliance tracking dashboard"""
    records = ComplianceRecord.objects.filter(user=request.user).select_related('module')
    modules = ComplianceModule.objects.all()
    completed_ids = records.filter(passed=True).values_list('module_id', flat=True)
    
    stats = {
        'total': modules.count(),
        'completed': len(set(completed_ids)),
        'pending': modules.count() - len(set(completed_ids)),
        'compliance_rate': round(len(set(completed_ids)) / max(modules.count(), 1) * 100, 1),
    }

    return render(request, 'compliance/compliance_dashboard.html', {
        'records': records,
        'stats': stats,
        'modules': modules,
    })

@login_required
def download_certificate(request, cert_id):
    from django.http import HttpResponse
    record = get_object_or_404(ComplianceRecord, certificate_id=cert_id, user=request.user, passed=True)
    
    html_content = f"""
    <html><head><title>Compliance Certification</title>
    <style>
        body {{ font-family: 'Arial', sans-serif; text-align: center; background: #f0f4f8; padding: 50px; }}
        .cert-box {{ border: 10px solid #f9d423; padding: 50px; background: white; max-width: 800px; margin: 0 auto; box-shadow: 0 10px 30px rgba(0,0,0,0.1); }}
        h1 {{ color: #1a1a3e; font-size: 40px; margin-bottom: 20px; }}
        h2 {{ color: #4facfe; font-size: 30px; margin-bottom: 30px; }}
        p {{ font-size: 20px; color: #555; line-height: 1.5; margin-bottom: 20px; }}
        .name {{ font-size: 35px; font-weight: bold; color: #667eea; text-transform: uppercase; margin: 20px 0; border-bottom: 2px solid #f9d423; display: inline-block; padding-bottom: 10px; }}
        .footer {{ margin-top: 50px; font-size: 14px; color: #777; display: flex; justify-content: space-between; }}
    </style>
    </head><body>
    <div class="cert-box">
        <h1>Official Compliance Certification</h1>
        <p>This certifies that</p>
        <div class="name">{record.user.get_full_name() or record.user.username}</div>
        <p>has successfully completed the mandatory training requirements for</p>
        <h2>{record.module.title}</h2>
        <p>with a passing score of <strong>{record.percentage}%</strong></p>
        <p style="font-size: 16px; margin-top: 30px;">This demonstrates compliance with {record.module.get_regulation_display()} standards.</p>
        <div class="footer">
            <span>Date Issued: {record.completion_date.strftime('%B %d, %Y')}</span>
            <span>Verification ID: {record.certificate_id}</span>
        </div>
        <div style="margin-top: 40px;">
            <button onclick="window.print()" style="padding: 10px 20px; background: #f9d423; color: #1a1a3e; font-weight: bold; border: none; cursor: pointer; border-radius: 5px;">Print / Save as PDF</button>
        </div>
    </div>
    </body></html>
    """
    return HttpResponse(html_content)
