from django.shortcuts import render, HttpResponse, redirect
from .models import User
from django.contrib import messages

# Create your views here.
# index "/"
def index(request):
    # User.objects.all().delete()
    return render(request, "beltbelt/index.html")

def register(request):
    results = User.objects.validate(request.POST)   # Returned results from validation. 
    if results['status'] == True:
        user = User.objects.creator(request.POST)
        messages.success(request, "User successfully created!!")
    else:
        for error in results['errors']:
            messages.error(request, error)            
    return redirect("/")

def login(request):    
    results = User.objects.loginVal(request.POST)
    if results['status'] == False:
        messages.error(request, 'Please  check your email or password and try again!')
        return redirect('/')
    request.session['email'] = results['user'].email
    request.session['first_name'] = results['user'].first_name          
    return redirect('dashboard/books.html')  

def logout(request):    
    request.session.flush()
    return redirect('/')


