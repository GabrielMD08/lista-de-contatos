from django import forms
<<<<<<< HEAD
from . import models

class ContactForm(forms.ModelForm):
    
    class Meta:
        model = models.Contact
        fields = '__all__'

        

=======
from .models import Contact


class ContactForm(forms.ModelForm):
    
    class meta:
        model = Contact
        fields = '__all__'

>>>>>>> contactsModel
        labels = {
            'first_name': 'Nome',
            'last_name' : 'Sobrenome',
            'nick_name' : 'Apelido',
<<<<<<< HEAD
            'phone_number' : 'Celular/Telefone',
            'email' : 'Email'
        }
=======
            'phone_number' : 'Numero do celular/telefone',
            'email' : 'Email'
        }
        
>>>>>>> contactsModel
