from django.shortcuts import render, redirect, get_object_or_404
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

    return render(request, 'contacts_list.html', context)

def update_contact(request, pk):
    contact = get_object_or_404(models.Contact, pk=pk)
    if request.method == 'POST':
        form = forms.ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contacts:contacts_list')
    else:
        form = forms.ContactForm(instance=contact)

    return render(request, 'new_contact.html', {'form': form, 'contact': contact})