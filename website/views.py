from django.shortcuts import render ,redirect
from django.contrib.auth import authenticate , login ,logout 
from django.contrib import messages 
from .forms import SignUpForm

# Create your views here.

def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #Authenticate
        user = authenticate(request , username = username , password = password)
        if user is not None:
            login(request ,user)
            messages.success(request,'You Have logged in ')
            return redirect('home')
        else:
           messages.success(request,'there is error happened')
           return redirect('home')
    else:   
     return render( request ,'home.html',{})


def logout_user(request):
    logout(request)
    messages.success(request,'you have been logout')
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
          form = SignUpForm(request.POSt)
          if form.is_valid() :
              form.save()
              
    return render( request ,'register.html',{})