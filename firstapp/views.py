from urllib import request
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login ,logout  #django authendicarion (login logout)




def user_login(request):
    # if 'username' in request.session:     /// another method session authendication 
    if request.user.is_authenticated:   #django authendication
        return redirect(home)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
     
        user = authenticate(username=username, password=password)
        if user is not None:   # means if user is authendicated
            #request.session['username'] = username  /// another method
            login(request, user)
            return redirect(home)
        else:
            print('invalid credentials')
    return render(request, 'login.html')

def home(request):
    # if 'username' in request.session:     /// another method
    if request.user.is_authenticated:
        return render(request, 'home.html')
   
    return redirect(user_login)
    
def user_logout(request):
    # if 'username' in request.session:     /// another method
    if request.user.is_authenticated:

        request.session.flush()
    return redirect(user_login)
