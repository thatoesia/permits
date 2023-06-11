from django.shortcuts import render, redirect
from .forms import RegistrationForm, UpdateUserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            first_name = form.cleaned_data.get('first_name')
            messages.success(request, f'Account created for {first_name}, check your email and follow all the steps! ')
            return redirect('login')
        messages.error(request, 'unsuccessful registration invalid information')
    form = RegistrationForm()

    context = {
        'form': form,
    }

    return render(request, 'register.html', context)


@login_required()
def profile(request):
    if request.method == 'POST':
        form = UpdateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'your profile has been updated!')
            return redirect('profile')
        else:
            messages.error(request, f'your profile has some errors!')
    else:
        form = UpdateUserForm(instance=request.user)

    context = {
        'form': form,
    }

    return render(request, 'profile.html', context)