from django.urls import path
from . import views

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('order_success/<order_number>', views.checkout_achievement, name='check_success'),
]