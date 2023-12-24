from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductsList.as_view(), name='products'),
    path('category/<category>/',
         views.ProductsList.as_view(), name='products_by_category'),
    path('catalogue/<brand_auto>/', 
         views.ProductsList.as_view(), name='products_by_brand_auto'),
    path('brand/<product_brand>/', 
         views.ProductsList.as_view(), name='products_by_product_brand'),
    path('item/<slug:slug>', views.product_detail, name='product_detail'),
]
