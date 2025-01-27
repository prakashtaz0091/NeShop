from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from shop.models import Product
from .models import CartProduct, Cart


@login_required(login_url='login_view')
def cart_view(request):
    try:
        cart = Cart.objects.get(user=request.user)
        cart_products = CartProduct.objects.select_related('product').filter(cart=cart)  
    except Exception as e:
        print(e)
        return redirect('shop_view')   
    else:
        # for product in cart_products:
        #     print(product.product.name)
        context = {
            'products': cart_products
        }
        return render(request, 'cart/cart.html', context)


@login_required(login_url='login_view')
def add_to_cart_view(request, product_id):
    
    try:
        product = Product.objects.get(id=product_id)
        cart = Cart.objects.get(user=request.user)
    except Product.DoesNotExist:
        return redirect('shop_view')
    except Cart.DoesNotExist:
        return redirect('shop_view')
    except Exception as e:
        print(e)
        return redirect('shop_view')
    else:
        try:
            CartProduct.objects.create(
                cart = cart,
                product = product,
            )
        except Exception as e:
            print(e)
            return redirect('shop_view')
        else:
            return redirect('cart_view')
    
    
    
