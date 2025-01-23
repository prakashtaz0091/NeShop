from django.shortcuts import render, redirect
from django.contrib.auth.password_validation import validate_password
from .models import CustomUser
from django.contrib.auth import authenticate, login, logout


def login_view(request):
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if not email or not password:
            return render(request, 'account/login.html', {'error': 'All fields are required'})
        
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('shop_view')
        
        return render(request, 'account/login.html', {'error': 'Invalid credentials'})
        
    
    
    return render(request, 'account/login.html')


def register(request):
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        user_type = request.POST.get('user_type')
        
        if not email or not password or not confirm_password or not user_type:
            return render(request, 'account/register.html', {'error': 'All fields are required'})
        
        if password != confirm_password:
            return render(request, 'account/register.html', {'error': 'Passwords do not match'})
        
        
        
        try:
            validate_password(password)
        except Exception as e:
            # print(type())
            return render(request, 'account/register.html', {'errors':list(e) })
        else:
            new_user = CustomUser.objects.create_user(email=email, password=password, user_type=user_type)

            if new_user:
                return redirect('login_view')
        
        # Rest of your registration logic
        
        
    
    return render(request, 'account/register.html')
