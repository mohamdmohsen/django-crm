from django.shortcuts import render ,redirect
from django.contrib.auth import authenticate , login ,logout 
from django.contrib import messages 
from .forms import SignUpForm ,AddRecordForm
from .models import Record 
from django.contrib.auth.decorators import login_required 
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def home(request):
    records = Record.objects.all()

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
     return render( request ,'home.html',{'records': records})


def logout_user(request):
    logout(request)
    messages.success(request,'you have been logout')
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
          form = SignUpForm(request.POST)
          if form.is_valid() :
              form.save()
              messages.success(request, 'You Have Successfully Registered !')
              return redirect('home')
    else:
        form = SignUpForm()      
    return render( request ,'register.html',{'form':form})    

@login_required
def customer_record(request,pk):
    customer_record = Record.objects.get( id=pk)
    return render( request ,'record.html',{"customer_record":customer_record}) 

@login_required
def delete_customer(request,pk):
    if request.method == 'POST':

        delete_it = Record.objects.get(id = pk)
        delete_it.delete()
        messages.success(request,"Customers has been deleted")
    return redirect("home")
@login_required
def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            add_record = form.save()
            messages.success(request,"Customer Added Successfully!")
            return redirect("home")

    return render( request ,'add_record.html',{"form":form}) 
@login_required
def update_record(request,pk):
    current_record = Record.objects.get(id=pk)
    form = AddRecordForm(request.POST or None,instance= current_record)
    if form.is_valid():
        form.save()
        messages.success(request, "Customer Updated Successfully!")
        return redirect("home")
    return render(request,"update_record.html",{"form": form })
    


