from django.shortcuts import render
from django.urls import reverse
from . import forms

def index(request):
    return reverse('index')

def new_contact(request):
    
    if request.method == 'POST':
        
        form = forms.ContactForm(request.POST)

        if form.is_valid():
            form.save()

            return reverse('index')
    
    else :
        form = forms.ContactForm()
    
    return render(request, 'templates/new_contact', {'form': form})