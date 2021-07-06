from django.shortcuts import redirect, render
from .models import placeholder
from django.contrib.auth.models import User , auth
from django.contrib import messages
# Create your views here.


def register(request):
    place = placeholder.objects.all()
    if request.method  == 'POST':
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        username= request.POST['user_name']
        email = request.POST['mail_id']
        phoneno = request.POST['phone_no']
        password1 = request.POST['password']
        password2 = request.POST['password1']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username already exists')
                return redirect('register')
            elif password1.isalnum() and len(password1) >= 8:
                user = User.objects.create_user(username=username, password=password1)
                user.save()
                messages.info(request,"You have been registered. Please login.")
                return redirect('/')
            else:    
                messages.info(request,"Password doesn\'t match the requirements.")
                return redirect('register')
        else:
            messages.info(request,'Passwords don\'t match.')
            return redirect('register')    
    else:
        return render(request,'register.html',{'place':place})
       

           
