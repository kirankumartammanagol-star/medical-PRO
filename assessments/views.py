from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Assessment, Question, AssessmentResult


@login_required
def assessment_list(request):
    """List all available assessments"""
    assessments = Assessment.objects.filter(is_active=True)
    categories = Assessment.CATEGORY_CHOICES
    selected_category = request.GET.get('category', '')
    if selected_category:
        assessments = assessments.filter(category=selected_category)

    user_results = AssessmentResult.objects.filter(user=request.user).values_list('assessment_id', flat=True)

    return render(request, 'assessments/assessment_list.html', {
        'assessments': assessments,
        'categories': categories,
        'selected_category': selected_category,
        'completed_ids': list(user_results),
    })


@login_required
def take_assessment(request, pk):
    """Take an assessment quiz"""
    assessment = get_object_or_404(Assessment, pk=pk, is_active=True)
    
    if AssessmentResult.objects.filter(user=request.user, assessment=assessment, passed=True).exists():
        messages.info(request, "You have already passed this assessment.")
        return redirect('assessments:results')
        
    questions = assessment.questions.all().order_by('?')[:assessment.total_questions]

    if request.method == 'POST':
        score = 0
        total = questions.count()
        answers = {}

        for question in questions:
            user_answer = request.POST.get(f'question_{question.id}', '')
            answers[str(question.id)] = user_answer
            if user_answer.lower().strip() == question.correct_answer.lower().strip():
                score += question.points

        percentage = (score / max(total, 1)) * 100
        passed = percentage >= assessment.passing_score

        # AI Feedback Generation (Mocked for offline)
        weak_topics = []
        if not passed:
            weak_topics.append("Review standard protocols for " + assessment.get_category_display())
        
        ai_feedback = f"AI Analysis: You demonstrated {'excellent' if percentage > 80 else 'adequate' if passed else 'needs improvement'} knowledge. "
        if weak_topics:
            ai_feedback += f"Focus on: {', '.join(weak_topics)}."

        result = AssessmentResult.objects.create(
            user=request.user,
            assessment=assessment,
            score=score,
            total_points=total,
            percentage=round(percentage, 1),
            passed=passed,
            answers=answers,
            validation_notes=ai_feedback
        )
        
        if passed:
            from .models import Certificate
            import uuid
            Certificate.objects.create(
                user=request.user, 
                assessment=assessment, 
                result=result,
                certificate_id=str(uuid.uuid4())[:8].upper()
            )

        if passed:
            messages.success(request, f'Congratulations! You passed with {percentage:.0f}%!')
        else:
            messages.warning(request, f'You scored {percentage:.0f}%. Required: {assessment.passing_score}%.')

        return redirect('assessments:results')

    return render(request, 'assessments/take_assessment.html', {
        'assessment': assessment,
        'questions': questions,
    })


@login_required
def assessment_results(request):
    """View assessment results"""
    results = AssessmentResult.objects.filter(user=request.user).select_related('assessment')
    stats = {
        'total_taken': results.count(),
        'passed': results.filter(passed=True).count(),
        'avg_score': 0,
    }
    if results.exists():
        stats['avg_score'] = round(sum(r.percentage for r in results) / results.count(), 1)

    return render(request, 'assessments/results.html', {
        'results': results,
        'stats': stats,
    })

@login_required
def leaderboard(request):
    top_scores = AssessmentResult.objects.filter(passed=True).order_by('-percentage', 'time_taken_minutes')[:20]
    return render(request, 'assessments/leaderboard.html', {'top_scores': top_scores})

@login_required
def download_certificate(request, pk):
    from django.http import HttpResponse
    from .models import Certificate
    cert = get_object_or_404(Certificate, pk=pk, user=request.user)
    
    # In a real app, generate a PDF using ReportLab or WeasyPrint.
    # Here we return a simple printable HTML representation.
    html_content = f"""
    <html><head><title>Certificate of Completion</title>
    <style>
        body {{ font-family: 'Arial', sans-serif; text-align: center; background: #f0f4f8; padding: 50px; }}
        .cert-box {{ border: 10px solid #667eea; padding: 50px; background: white; max-width: 800px; margin: 0 auto; box-shadow: 0 10px 30px rgba(0,0,0,0.1); }}
        h1 {{ color: #1a1a3e; font-size: 40px; margin-bottom: 20px; }}
        h2 {{ color: #00d4aa; font-size: 30px; margin-bottom: 30px; }}
        p {{ font-size: 20px; color: #555; line-height: 1.5; margin-bottom: 20px; }}
        .name {{ font-size: 35px; font-weight: bold; color: #667eea; text-transform: uppercase; margin: 20px 0; border-bottom: 2px solid #00d4aa; display: inline-block; padding-bottom: 10px; }}
        .footer {{ margin-top: 50px; font-size: 14px; color: #777; display: flex; justify-content: space-between; }}
    </style>
    </head><body>
    <div class="cert-box">
        <h1>Certificate of Excellence</h1>
        <p>This is to certify that</p>
        <div class="name">{cert.user.get_full_name() or cert.user.username}</div>
        <p>has successfully completed the assessment</p>
        <h2>{cert.assessment.title}</h2>
        <p>with a score of <strong>{cert.result.percentage}%</strong></p>
        <div class="footer">
            <span>Date: {cert.issue_date.strftime('%B %d, %Y')}</span>
            <span>Certificate ID: {cert.certificate_id}</span>
        </div>
        <div style="margin-top: 40px;">
            <button onclick="window.print()" style="padding: 10px 20px; background: #667eea; color: white; border: none; cursor: pointer; border-radius: 5px;">Print / Save as PDF</button>
        </div>
    </div>
    </body></html>
    """
    return HttpResponse(html_content)
