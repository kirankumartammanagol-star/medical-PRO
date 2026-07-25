from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Simulation, SimulationStep, SimulationAttempt


@login_required
def simulation_list(request):
    """List all available clinical simulations"""
    simulations = Simulation.objects.filter(is_active=True)
    scenario_types = Simulation.SCENARIO_TYPES
    selected_type = request.GET.get('type', '')
    if selected_type:
        simulations = simulations.filter(scenario_type=selected_type)

    user_attempts = SimulationAttempt.objects.filter(user=request.user).values_list('simulation_id', flat=True)

    return render(request, 'simulations/simulation_list.html', {
        'simulations': simulations,
        'scenario_types': scenario_types,
        'selected_type': selected_type,
        'attempted_ids': list(user_attempts),
    })


@login_required
def virtual_patient(request, pk):
    """Virtual patient simulation interface"""
    simulation = get_object_or_404(Simulation, pk=pk, is_active=True)
    steps = simulation.steps.all()

    if request.method == 'POST':
        score = 0
        total = steps.count()
        responses = {}

        for step in steps:
            user_answer = request.POST.get(f'step_{step.id}', '')
            responses[str(step.id)] = user_answer
            if user_answer.upper() == step.correct_option.upper():
                score += 1

        percentage = (score / max(total, 1)) * 100

        if percentage >= 80:
            feedback = "Excellent clinical judgment! You demonstrated strong diagnostic and treatment skills."
            hiring_recommendation = 'highly_recommended'
            patient_outcome = 'excellent'
        elif percentage >= 60:
            feedback = "Good performance. Consider reviewing the areas where you chose different approaches."
            hiring_recommendation = 'recommended'
            patient_outcome = 'good'
        else:
            feedback = "This simulation highlighted areas for improvement. Review the clinical guidelines and try again."
            hiring_recommendation = 'not_recommended'
            patient_outcome = 'poor'

        improvements = []
        if percentage < 100:
            improvements.append("Review clinical guidelines for standard protocols.")
        if percentage < 80:
            improvements.append("Improve diagnostic speed and accuracy.")

        SimulationAttempt.objects.create(
            user=request.user,
            simulation=simulation,
            responses=responses,
            score=score,
            percentage=round(percentage, 1),
            feedback=feedback,
            patient_outcome=patient_outcome,
            hiring_recommendation=hiring_recommendation,
            recommended_improvements=improvements,
            competency_assessment={"accuracy": percentage, "safety": 100 if percentage >= 80 else 50}
        )

        messages.info(request, f'Simulation completed! Score: {percentage:.0f}%')
        return redirect('simulations:simulation_results')

    return render(request, 'simulations/virtual_patient.html', {
        'simulation': simulation,
        'steps': steps,
    })


@login_required
def simulation_results(request):
    """View simulation results and feedback"""
    attempts = SimulationAttempt.objects.filter(user=request.user).select_related('simulation')
    stats = {
        'total': attempts.count(),
        'avg_score': 0,
    }
    if attempts.exists():
        stats['avg_score'] = round(sum(a.percentage for a in attempts) / attempts.count(), 1)

    return render(request, 'simulations/simulation_results.html', {
        'attempts': attempts,
        'stats': stats,
    })

@login_required
def download_sim_certificate(request, attempt_id):
    from django.http import HttpResponse
    attempt = get_object_or_404(SimulationAttempt, id=attempt_id, user=request.user)
    if attempt.percentage < 80:
        return redirect('simulations:simulation_results')
    
    html_content = f"""
    <html><head><title>Clinical Simulation Certification</title>
    <style>
        body {{ font-family: 'Arial', sans-serif; text-align: center; background: #f0f4f8; padding: 50px; }}
        .cert-box {{ border: 10px solid #00b4d8; padding: 50px; background: white; max-width: 800px; margin: 0 auto; box-shadow: 0 10px 30px rgba(0,0,0,0.1); }}
        h1 {{ color: #1a1a3e; font-size: 40px; margin-bottom: 20px; }}
        h2 {{ color: #0077b6; font-size: 30px; margin-bottom: 30px; }}
        p {{ font-size: 20px; color: #555; line-height: 1.5; margin-bottom: 20px; }}
        .name {{ font-size: 35px; font-weight: bold; color: #00b4d8; text-transform: uppercase; margin: 20px 0; border-bottom: 2px solid #03045e; display: inline-block; padding-bottom: 10px; }}
        .footer {{ margin-top: 50px; font-size: 14px; color: #777; display: flex; justify-content: space-between; }}
    </style>
    </head><body>
    <div class="cert-box">
        <h1>Clinical Competency Certification</h1>
        <p>This certifies that</p>
        <div class="name">{attempt.user.get_full_name() or attempt.user.username}</div>
        <p>has successfully passed the Clinical Simulation Assessment for</p>
        <h2>{attempt.simulation.title}</h2>
        <p>with an outstanding score of <strong>{attempt.percentage}%</strong></p>
        <p style="font-size: 16px; margin-top: 30px;">Competency Rating: {attempt.get_hiring_recommendation_display()}</p>
        <div class="footer">
            <span>Date Issued: {attempt.completed_at.strftime('%B %d, %Y')}</span>
            <span>Verification ID: SIM-{attempt.id}</span>
        </div>
        <div style="margin-top: 40px;">
            <button onclick="window.print()" style="padding: 10px 20px; background: #00b4d8; color: white; font-weight: bold; border: none; cursor: pointer; border-radius: 5px;">Print / Save as PDF</button>
        </div>
    </div>
    </body></html>
    """
    return HttpResponse(html_content)
