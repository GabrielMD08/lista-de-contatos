from django.db import models
from django.core.validators import RegexValidator

class Contact(models.Model):
    first_name = models.CharField('Nome', max_length=30)
    last_name = models.CharField('Sobrenome', max_length=60, null=True, blank=True )
    nick_name = models.CharField('Apelido', max_length=30, null=True, blank=True)

    phone_validator = RegexValidator(
            regex= r'^\+55\d{10,11}',
            message= 'Numero invalido! Use o Formato +55 (XX) 9XXXX-XXXX'
            )

    phone_number = models.CharField('Numero de telefone', max_length=14, validators=[phone_validator], unique=True)
    email = models.EmailField('Email', null=True, blank=True)

    def __str__(self):
        return f'{self.first_name}'
    
    def show_full_name(self):
        if self.last_name == None:
            return f'{self.first_name}'
        else:
            return f'{self.first_name} {self.last_name}'
        
    def show_nick_name(self):
        return f'{self.nick_name}'
