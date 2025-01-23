from django.shortcuts import render, redirect
from django.contrib.auth.password_validation import validate_password
from .models import CustomUser



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
                return redirect('account/login.html')
        
        # Rest of your registration logic
        
        
    
    return render(request, 'account/register.html')
