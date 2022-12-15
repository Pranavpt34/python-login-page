from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from .forms import UserRegisterForm
from django.views.decorators.cache import never_cache

# Create your views here.


@never_cache
def base_file(request):
    if 'username' in request.session:
        return render(request, 'base.html')
    else:
        return redirect('login')


@never_cache
def user_login(request):
    if 'username' in request.session:
        return redirect('base_file')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            request.session['username'] = username
            return redirect('base_file')
        else:
            print('invalid ')
    return render(request, 'login.html')


def user_logout(request):
    if 'username' in request.session:
        del request.session['username']
    return redirect('login')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})


