from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render

def logout_client(request):
    logout(request)
    return HttpResponseRedirect('/')

def login_client(request):
    message = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(request.GET['next'])
            else:
                # Return a 'disabled account' error message
                pass
        else:
            message = 'Неверный логин/пароль'
            return render(request, 'login.html', locals())


    return render(request, 'login.html', locals())