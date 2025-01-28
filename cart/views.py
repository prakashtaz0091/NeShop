from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from shop.models import Product
from .models import CartProduct, Cart, State, District, Municipality, DeliveryAddress, Order
# from django.db.models import Prefetch
from django.views.decorators.http import require_POST


@login_required(login_url='login_view')
@require_POST
def place_order(request):
    delivery_address_id = request.POST.get('delivery-address')
    payment_method = request.POST.get('payment-method')
    product_id = request.POST.get('product-id')
    
    try:
        address = DeliveryAddress.objects.get(id=delivery_address_id)
        cart_product = CartProduct.objects.get(id=product_id)
    except DeliveryAddress.DoesNotExist:
        return redirect("cart_view")
    else:
        try:
            order = Order.objects.create(
                product = cart_product,
                delivery_address = address,
                payment_method = payment_method
            ) 
        except Exception as e:
            print(e) 
        else:
            cart_product.ordered = True
            cart_product.save()
        finally:
            return redirect("cart_view")   
        
              




@login_required(login_url='login_view')
@require_POST
def add_delivery_address(request):
    state_id = request.POST.get('state-id')
    district_id = request.POST.get('district-id')
    municipality_id = request.POST.get('municipality-id')
    local_address = request.POST.get('local-address')
    cart_product_id = request.POST.get('cart_product_id')
    
    try:
        state = State.objects.get(id=state_id)
        district = District.objects.get(id=district_id)
        municipality = Municipality.objects.get(id=municipality_id)
    except Exception as e:
        print(e)
        return redirect("checkout", cart_product_id=cart_product_id)
    else:
        try:
            DeliveryAddress.objects.create(
                user = request.user,
                state = state,
                district = district,
                municipality = municipality,
                local_address = local_address
            )
        except Exception as e:
            print(e)
        finally:
            return redirect("checkout", cart_product_id=cart_product_id)
        

    
    
    
@login_required(login_url='login_view')
def checkout(request, cart_product_id):
    
    quantity = request.GET.get('quantity')
    
    
    try:
        cart_product = CartProduct.objects.get(
            id=cart_product_id
        )
        if quantity:
            cart_product.quantity = int(quantity)
            cart_product.save()
            print(cart_product.quantity)
        states = State.objects.all()
        districts = District.objects.all()
        municipalities = Municipality.objects.all()
        delivery_addresses = DeliveryAddress.objects.filter(user=request.user)
    except CartProduct.DoesNotExist:
        print("cart product not exist")
        return redirect("cart_view")
    else:
        
        
        
        context = {
            'product':cart_product,
            'states':states,
            'districts':districts,
            'municipalities':municipalities,
            'delivery_addresses':delivery_addresses
            
        }
        return render(request, "cart/product_checkout.html", context)



@login_required(login_url='login_view')
def delete_product_from_cart(request, cart_product_id):
    
    if request.method == "POST":
        cart_product_id = request.POST.get("product_id", None)
        if cart_product_id is not None:
            try:
                cart_product = CartProduct.objects.get(id=cart_product_id)
            except CartProduct.DoesNotExist:
                return redirect("cart_view")
            else:
                cart_product.delete()
                return redirect("cart_view")

    
    try:
        cart_product = CartProduct.objects.get(
            id=cart_product_id
        )
    except CartProduct.DoesNotExist:
        print("cart product not exist")
        return redirect("cart_view")
    else:
        context = {
            'product': cart_product
        }
        return render(request, "cart/cart_product_delete.html", context)
    
    


@login_required(login_url='login_view')
def cart_view(request):
    try:
        cart = Cart.objects.get(user=request.user)
        cart_products = CartProduct.objects.select_related('product').filter(cart=cart, ordered=False)  
    except Exception as e:
        print(e)
        return redirect('shop_view')   
    else:
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
    
    
    
