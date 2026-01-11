from django import forms
from . import models

class ContactForm(forms.ModelForm):
    
    class Meta:
        model = models.Contact
        fields = '__all__'

        

        labels = {
            'first_name': 'Nome',
            'last_name' : 'Sobrenome',
            'nick_name' : 'Apelido',
            'phone_number' : 'Celular/Telefone',
            'email' : 'Email'
        }