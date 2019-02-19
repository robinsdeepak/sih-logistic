from django.urls import path
from price_calculator import views

name = 'price_calculator'
urlpatterns = [
    path('calculate_price/', views.Calculate, name='calculate')
]
