from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('order_success/<order_number>', views.checkout_achievement,
         name='check_success'),
    path('wh/', webhook, name='webhook'),
]
