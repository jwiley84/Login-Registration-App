from django.shortcuts import render, HttpResponse, redirect
from apps.LoginRegistrationApp.models import *
from django.contrib import messages
import bcrypt
#from apps.LoginRegistrationApp.models import UserManager

def index(request):
	# response = "THIS IS DONE"
	return render(request, 'LoginRegistrationApp/index.html')

def register(request):
    ## ROUGH ## 
    ## NO HASHING ##
    errors = User.objects.basic_validator(request.POST)
    already_user = User.objects.filter(email = request.POST['email'])
    print(already_user)
    if len(errors):
        for tag, error in errors.items():
            messages.error(request, error)
        return redirect('/')
    elif len(already_user) > 0:
        error = "This email has already been registered, please login instead"
        messages.error(request, error)
        return redirect('/')        
    else:
        user = User.objects.create();
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
              
        password = request.POST['password']
        hash_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt());
        user.password = hash_pw

        # The password attribute of a User object is a string in this format:
        # <algorithm>$<iterations>$<salt>$<hash>
        if not request.POST['birthday']:
            user.birthday = None;
        else:
            user.birthday = request.POST['birthday']
        user.save();
        request.session['id'] = user.id
        # print(user.birthday)
        return redirect('/success')

def login(request):
    errors = User.objects.login_validator(request.POST)
    user = User.objects.filter(email = request.POST['email'])
    #check for not registered 
    if len(errors):
        for tag, error in errors.items():
            messages.error(request, error)
        return redirect('/')
    elif len(user) < 1:
        error = "No registered account under that email. Please check the spelling, or register to the left"
        messages.error(request, error)
        return redirect('/')
    else:
        check_pass = request.POST['password']
        test = bcrypt.checkpw(check_pass.encode(), user[0].password.encode())
        print(test)
        print(user[0].password)
        if test == False:
            error = "Incorrect password. Please check spelling and try again. Password reset system is currently offline"
            messages.error(request, error)
            return redirect('/')
        else:
            return redirect('/success')

def success(request):
    pass_ID = request.session['id']
    print(pass_ID)
    user = User.objects.filter(id = pass_ID)
    print(user)
    request.session['name'] = user[0].first_name
    return render(request, 'LoginRegistrationApp/success.html')