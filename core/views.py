from django.shortcuts import render
from django.urls import reverse
from . import forms

def index(request):

    context = {
        'titulo': 'Bem-vindo!'
    }

    return render(request, 'templates/index.html', context)