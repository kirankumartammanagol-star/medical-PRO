from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .models import Credential, VerificationRequest


@login_required
def credential_list(request):
    """List all credentials for the logged-in user"""
    credentials = Credential.objects.filter(user=request.user)
    stats = {
        'total': credentials.count(),
        'verified': credentials.filter(status='verified').count(),
        'pending': credentials.filter(status='pending').count(),
        'expired': credentials.filter(status='expired').count(),
    }
    return render(request, 'credentials/credential_list.html', {
        'credentials': credentials,
        'stats': stats,
    })


@login_required
def credential_submit(request):
    """Submit a new credential for verification"""
    if request.method == 'POST':
        credential = Credential.objects.create(
            user=request.user,
            credential_type=request.POST.get('credential_type'),
            title=request.POST.get('title'),
            license_number=request.POST.get('license_number'),
            issuing_authority=request.POST.get('issuing_authority'),
            issuing_state=request.POST.get('issuing_state', ''),
            issue_date=request.POST.get('issue_date'),
            expiry_date=request.POST.get('expiry_date') or None,
            notes=request.POST.get('notes', ''),
        )
        if request.FILES.get('document'):
            credential.document = request.FILES['document']
            credential.save()

        VerificationRequest.objects.create(
            credential=credential,
            requested_by=request.user,
            verification_notes='Auto-submitted for verification'
        )
        messages.success(request, 'Credential submitted successfully for verification!')
        return redirect('credentials:credential_list')

    return render(request, 'credentials/credential_submit.html')


@login_required
def verification_dashboard(request):
    """Dashboard for viewing verification statuses"""
    all_requests = VerificationRequest.objects.select_related('credential', 'credential__user').order_by('-created_at')
    my_credentials = Credential.objects.filter(user=request.user)
    return render(request, 'credentials/verification_dashboard.html', {
        'verification_requests': all_requests[:20],
        'my_credentials': my_credentials,
    })


@login_required
def credential_detail(request, pk):
    """View credential details"""
    credential = get_object_or_404(Credential, pk=pk)
    return render(request, 'credentials/credential_detail.html', {'credential': credential})
