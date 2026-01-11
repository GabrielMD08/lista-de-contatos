from django.urls import path
from . import views

app_name = 'contacts'

urlpatterns = [
    path('new-contact/', views.new_contact, name='new_contact'),
    path('contacts-list', views.contacts_list, name='contacts_list'),
]
