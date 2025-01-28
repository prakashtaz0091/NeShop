from django.urls import path
from .views import *

urlpatterns = [
    path('', cart_view, name='cart_view'),
    path('add/<int:product_id>/', add_to_cart_view, name='add_to_cart_view'),
    path('delete/<int:cart_product_id>/', delete_product_from_cart, name='delete_product_from_cart'),
    path('checkout/<int:cart_product_id>/', checkout, name='checkout'),
    path('delivery-address/add/', add_delivery_address, name='add_delivery_address'),
    path('place-order/', place_order, name='place_order'),
    
    
]
