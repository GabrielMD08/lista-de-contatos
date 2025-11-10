from django.urls import path
from . import views

urlpatterns = [
    path('/', views.index, name='index'),
    path('novo-contato/', views.new_contact, name='novo contato'),
]
