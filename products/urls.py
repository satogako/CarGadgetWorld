from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductsList.as_view(), name='products'),
    path('category/<category>/',
         views.ProductsList.as_view(), name='products_by_category'),
    path('item/<slug:slug>', views.product_detail, name='product_detail'),
]
