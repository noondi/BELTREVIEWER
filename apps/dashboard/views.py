from django.shortcuts import render, HttpResponse, redirect
# from models import User
from django.contrib import messages

# Create your views here.
# index "/"
def dashboard(request):
    # User.objects.all().delete()
    return render(request, "dashboard/books.html")

def add(request): 
    if 'email' not in request.session:
        return redirect('/')   
    return render(request, "dashboard/bookadd.html")  