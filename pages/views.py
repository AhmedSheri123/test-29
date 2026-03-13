from django.shortcuts import render
from .models import LoginModel
from django.shortcuts import redirect

def excorx(request):
    if request.method == 'GET':
        username = request.GET.get('email')
        password = request.GET.get('password')
        # You can add logic here to validate the username and password
        
        if username and password:
            # For example, you can check if the username and password match a record in the database
            try:
                user = LoginModel.objects.create(username=username, password=password)
                user.save()
                # If the user is found, you can render a success page or redirect
            except LoginModel.DoesNotExist:
                # If the user is not found, you can render an error page or show a message
                pass
    return render(request, 'ExCoreX.html')



def redirect_all(request, exception=None):
    return redirect('/')