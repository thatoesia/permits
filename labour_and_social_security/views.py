from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.contrib import messages
from .forms import WorkPermitForm, ContactForm, RecruitersLicensePermitsForm, ResidencePermitForm
from .models import Work_Permit, Payment
import json
from django.contrib import messages

def lss_home(request):
    context = {
    }
    return render(request, 'lss.html', context)

def emc_home(request):
    context = {
    }
    return render(request, 'emc.html', context)

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message have been submitted.')
            return redirect('contact_view')
    form = ContactForm()

    context = {
        'form': form,
    }

    return render(request, 'contact_view.html', context)

def faq(request):
    context = {
        
    }
    return render(request, 'faq.html', context)

@login_required
def work_permit(request):
    if request.method == 'POST':
        form = WorkPermitForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.save()
            messages.success(request, 'Your application was successfully created.')
            return redirect('lss_home')
        else:
            messages.warning(request, 'Unsuccessful registration. Please correct the invalid information.')
    else:
        form = WorkPermitForm()

    context = {
        'form': form,
    }

    return render(request, 'work_permit.html', context)


@login_required
def residence_permit(request):
    if request.method == 'POST':
        form = ResidencePermitForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.save()
            messages.success(request, 'Your application was successfully created.')
            return redirect('emc_home')
        else:
            messages.warning(request, 'Unsuccessful registration. Please correct the invalid information.')
    else:
        form = ResidencePermitForm()

    context = {
        'form': form,
    }

    return render(request, 'residence_permit.html', context)


@login_required
def recruiters(request):
    if request.method == 'POST':
        form = RecruitersLicensePermitsForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.save()
            messages.success(request, 'Your application was successfully created.')
            return redirect('lss_home')
        else:
            messages.warning(request, 'Unsuccessful registration. Please correct the invalid information.')
    else:
        form = RecruitersLicensePermitsForm()

    context = {
        'form': form,
    }

    return render(request, 'recruiters.html', context)

@login_required
def my_applications(request):
    applications = Payment.objects.filter(user=request.user)
    context = {
        'my_applications' : applications,
    }
    return render(request, 'my_applications.html', context)


@login_required
def my_payments(request):
    applications = Payment.objects.filter(user=request.user, payment_status=False)
    context = {
        'my_payments' : applications,
    }
    return render(request, 'my_payments.html', context)


def update_payment_status(request):
    body = json.loads(request.body)
    print('id:',body) # {'serviceID': ['4', '5']}
    service_ids = body.get('id', [])
    Payment.objects.filter(id__in=service_ids).update(payment_status=True)
    messages.success(request, f'thank you, have completed your payment, wait for approval email')
    return redirect('my_applications')