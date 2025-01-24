from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    #account
    path('account/', include('account.urls')),
    
    # #shop
    path('', include('shop.urls')),
    
    # #cart
    # path('cart/', include('cart.urls')),
    
    # #customer
    # path('customer/', include('customer.urls')),
    
    # #vendor
    # path('vendor/', include('vendor.urls')),
]
