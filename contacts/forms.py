from django import forms
from . import models

class ContactForm(forms.ModelForm):
    
    class meta:
        model = models.Contact
        fields = '__all__'

        labels = {
            'first_name': 'Nome',
            'last_name' : 'Sobrenome',
            'nick_name' : 'Apelido',
            'phone_number' : 'Numero do celular/telefone',
            'email' : 'Email'
        }