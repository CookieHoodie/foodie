from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import *

# Create your views here.
def register(request):
    if request.method == "POST":
        if request.POST.get('Cregister'):
            print("Cregister post")
            name = request.POST.get('dname')
            birth_date = request.POST.get('ddob')
            gender = request.POST.get('dgender')
            mobile_number = request.POST.get('dmnumber')
            email = request.POST.get('demail')
            password = request.POST.get('dpassword')

            record = Customer(name, birth_date, gender, mobile_number, email, password)

            try:
                user = User.objects.create_user(name, email, password)
            except:
                context = {'error_message': "Either username or email is used! Please use a new one."}
                return render(request, 'account/registration_form.html', context)

            record.save()
            return redirect('account:login')

        elif request.POST.get("Rregister"):
            print("Rregister post")
            name = request.POST.get('dname')
            email = request.POST.get('demail')
            password = request.POST.get('dpassword')
            nric = request.POST.get('dnric')
            office_number = request.POST.get('donumber')
            mobile_number = request.POST.get('dmnumber')
            gender = request.POST.get('dgender')
            birth_date = request.POST.get('ddob')
            record = Owner(name, birth_date, gender, nric, office_number, mobile_number, email, password)

            try:
                user = User.objects.create_user(name, email, password)
            except:
                context = {'error_message': "Either username or email is used! Please use a new one."}
                return render(request, 'account/registration_form.html', context)

            record.save()
            return redirect('account:login')

        else:
            context = {"error_message": "Please Enter Valid Details!"}
            return render(request, 'account/registration_form.html', context)
    return render(request, 'account/registration_form.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print("so far so good")
        if user is not None:
            login(request, user)
            return redirect('food:index')
        else:
            context = {"error_message": "Login Details Invalid!"}
            return render(request, 'account/login.html', context)

    return render(request, 'account/login.html')