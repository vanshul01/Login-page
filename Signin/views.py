from register.models import placeholder
from django.shortcuts import render,redirect 
from django.http import HttpResponse
from django.contrib.auth.models import User , auth
from django.contrib import messages
# Create your views here.
def home(request):
   # return HttpResponse('HelloWorld')
   #return render (request,'home.html')
   return render (request,'home.html',{'name':'vanshul'})

def add(request):
    val1=int (request.POST['num1'])
    val2=int (request.POST['num2']) 
    res =val1 + val2 

    return render (request,"result.html",{'result':res}) 

def login(request):
   
   place = placeholder.objects.all()
   if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user =auth.authenticate(username=username,password =password )
        

        if user is not None:
            auth.login(request,user)
            #messages.info(request,'login succusfully ')
            return redirect ('/home')

        else:
            messages.info(request,'invalid credentails ')
            return redirect('login')

   else:
        return render (request,'login.html',{'place':place})    

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
                return redirect('/register')
            elif password1.isalnum() and len(password1) >= 8:
                user = User.objects.create_user(username=username, password=password1, firstname=firstname)
                user.save()
                messages.info(request,"You have been registered. Please login.")
                return redirect('/')
            else:    
                messages.info(request,"Password doesn\'t match the requirements.")
                return redirect('/register')
        else:
            messages.info(request,'Passwords don\'t match.')
            return redirect('/register')    
    else:
        return render(request,'register.html',{'place':place})

def logout (request):
    auth.logout(request) 
    messages.info(request,'logout succusfully ')
    return redirect ('login')
           

