from urllib import request
from django.contrib import messages #passwrd incrrct time send  messg
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login ,logout  #django authendicarion (login logout)
#from django.contrib.auth.decorators import login_required  //3rd method


def user_login(request):
    # if 'username' in request.session:          /// 2nd method session authendication 
    if request.user.is_authenticated:            #django authendication
        return redirect(home)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password'] 
        user = authenticate(username=username, password=password)
        if user is not None:   # means if user is authendicated
            #request.session['username'] = username  /// 2nd method
            login(request, user)
            return redirect(home)
        else:
            messages.error(request,'username or password not correct')
            return redirect('user_login')
    return render(request, 'login.html')

#@login_required(login_url='/')                  //3rd method
def home(request):
    # if 'username' in request.session:          /// 2nd method
    if request.user.is_authenticated:
        return render(request, 'home.html')
   
    return redirect(user_login)


#@login_required(login_url='/')                    //3rd method
def user_logout(request):
    # if 'username' in request.session:           /// 2nd method
    if request.user.is_authenticated:
        logout(request)
        #request.session.flush()                     /// both
    return redirect(user_login)
