from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_wish_list, name='wish_list'),
    path('add/<int:product_id>/', views.add_to_wish_list,
         name='add_to_wish_list'),
    path('remove/<int:product_id>/', views.remove_from_wish_list,
         name='remove_from_wish_list'),
]
