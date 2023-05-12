from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.
def home(request):
    # Check to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Aunthenticate
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in!")
            return redirect ('Home')
        else:
            messages.success(request, "There was an error logging in, Please try again...")
            return redirect('Home')
    else:
        return render(request, 'home.html', {})


def login_user(request):
    pass

def logout_user(request):
    pass
