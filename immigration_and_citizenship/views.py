from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.contrib import messages


# Create your views here.
def home(request):
    context = {

    }
    return render(request, 'home.html', context)