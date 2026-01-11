from django.shortcuts import render, redirect
from django.urls import reverse
from . import forms, models

def new_contact(request):
    
    if request.method == 'POST':
        
        form = forms.ContactForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('index')
    
    else :
        form = forms.ContactForm()
    
    return render(request, 'new_contact.html', {'form': form})

def contacts_list(request):
    
    all_contacts = models.Contact.objects.all().order_by('first_name')

    context = {
        'title': 'Lista de Contatos',
        'contact_list': all_contacts,
    }

    return render(request, 'contact_list.html', context)