from django.shortcuts import render



def register(request):
    
    if request.method == 'POST':
        # user
        pass
    
    return render(request, 'account/register.html')
