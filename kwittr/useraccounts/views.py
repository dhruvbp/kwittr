from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


def user_login(request):
    context = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            # redirect to a success page.
            return redirect('frontpage')
        else:
            # render login again, but display error message
            context['login_failed'] = True
    # request.method == 'GET':
    return render(request, 'useraccounts/login.html', context)

def user_logout(request):
    logout(request)
    return redirect('frontpage')

"""Vi har lagt inn if for at den skal sjekke om brukernavn/email alerede existerer"""
def user_register(request):
    context = {}
    if request.method == "POST":
        new_user = request.POST.get('username').lower()
        if User.objects.filter(username=new_user).exists():
            context['username_already_exist'] = True
            return render(request, 'useraccounts/register.html', context)
        new_email = request.POST.get('email')
        if User.objects.filter(email=new_email).exists():
            context['email_already_exist'] = True
            return render(request, 'useraccounts/register.html', context)
        
        user = User()
        user.first_name = request.POST.get('firstname')
        user.last_name = request.POST.get('lastname')
        user.username = new_user
        user.email = new_email
        user.set_password(request.POST.get('password'))
        user.save()
        context['user_saved_successfully'] = True
    return render(request, 'useraccounts/register.html', context)

"""Brukeren må være logget inn for at man skal få lov til å endre profilen"""
@login_required
def user_profile(request):
    context = {}
    if request.method == "POST":
        user = request.user
        user.first_name = request.POST.get('firstname')
        user.last_name = request.POST.get('lastname')
        user.email = request.POST.get('email')
        user.save()
        context['user_saved_successfully'] = True
    return render(request, 'useraccounts/profile.html', context)



