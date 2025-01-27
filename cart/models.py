from django.db import models
from account.models import CustomUser
from shop.models import Product

class Cart(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)    
    products = models.ManyToManyField(Product, through="CartProduct", related_name="cart")
    
    def __str__(self):  
        return f"Cart for {self.user.email}"
    
    
class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    added_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f"{self.quantity} x {self.product.name} in {self.cart.user.email}'s cart"
    
    