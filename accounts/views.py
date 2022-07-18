from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.models import auth, User
from django.contrib import messages
# Create your views here.

def register(request):

    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']

        if User.objects.filter(username=username).exists():
            messages.info(request, "Username is already taken")
            return redirect('/')
        elif User.objects.filter(email=email).exists():
            messages.info(request, "Email is already taken")
            return redirect('/')
        elif password != confirmpassword:
            messages.info(request, "Password didn't match")
            return redirect('/')
        else:
            user = User.objects.create_user(first_name=firstname, last_name=lastname, email=email, username=username, password=password)
            user.save();
            return redirect('login/')


    return render(request, 'register.html')

def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('blog')
        else:
            messages.info(request, "Invalid username or password")
            return redirect('login')

    return render(request, 'login.html')