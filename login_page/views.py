from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.views.decorators.cache import never_cache
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def log_in(requast):
    if requast.user.is_authenticated:
        return redirect(home)

    if requast.method == 'POST':
        username = requast.POST['username']
        password = requast.POST['password']
        user = authenticate(username = username, password = password)
        if user is not None:
            login(requast, user)
            return redirect(home)
        else:
            error = 'username or password incorrect'
            return render(requast,'login.html', {'error': error})
    return render(requast, 'login.html')

@never_cache
def home(requast):
    if requast.user.is_authenticated:
        user_name = requast.user.username
        return render(requast, 'home.html', {'user_name': user_name})
    return redirect(log_in)



def log_out(requast):
    if requast.user.is_authenticated:
        logout(requast)
    return redirect(log_in)

def contact(requast):
    return render(requast, 'contact.html')


  