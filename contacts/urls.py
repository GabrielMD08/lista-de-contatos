from django.urls import path
from . import views

urlpatterns = [
    path('novo-contato/', views.new_contact, name='novo contato'),
]
