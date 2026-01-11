from django.shortcuts import render
from django.urls import reverse

def index(request):

    context = {
        'title': 'Bem-vindo!'
    }

    return render(request, 'index.html', context)