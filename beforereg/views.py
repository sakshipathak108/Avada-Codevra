from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .forms import UserForm
from django.shortcuts import render
from beforereg.models import register_table
from django.contrib.auth.models import User


def index(request):
    return render(request, 'beforereg/hats.html')


def contact(request):
    return render(request, 'beforereg/contact.html')


def signup(request):
    if request.method == 'POST':
        firname = request.POST['first_name']
        lastname = request.POST['last_name']
        emailid = request.POST['email']
        pwd = request.POST['password']
        skills_data = request.POST['skills']
        branch_data = request.POST['branch']

        usr = User.objects.create_user(username=emailid, email=emailid, password=pwd)
        usr.first_name = firname
        usr.last_name = lastname
        usr.set_password(pwd)
        usr.save()

        rex = register_table(user=usr, skills=skills_data, branch=branch_data)
        rex.save()
        return render(request, 'beforereg/signup.html',
                      {'alert': '{} your account is created successfully'.format(firname)})
    return render(request, 'beforereg/signup.html')


def loginuser(request):
    if request.method == 'POST':
        emailidd = request.POST['emaill']
        paswd = request.POST['passwordd']
        suser = User.objects.get(email=emailidd)

        detailsx = authenticate(username=emailidd, password=paswd)
        detailss = authenticate(username=suser.username, email=emailidd, password=paswd)
        if detailsx:
            login(request, detailsx)
            if detailsx.is_active:
                return render(request, 'beforereg/login.html', {'logalert': "Logged In Successfully"})
        if detailss:
            login(request, detailss)
            if detailss.is_superuser:
                return HttpResponseRedirect('/admin')

        else:
            return render(request, 'beforereg/login.html', {'alert': "Please enter correct credentials"})

    return render(request, 'beforereg/login.html')
