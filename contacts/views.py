from django.shortcuts import render, redirect
from django.urls import reverse
from . import forms

def new_contact(request):
    
    if request.method == 'POST':
        
        form = forms.ContactForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('index')
    
    else :
        form = forms.ContactForm()
    
    return render(request, 'new_contact.html', {'form': form})