from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, 'notes/index.html')

def login(request):
    if request.user.is_authenticated:
        return redirect('/notes_list')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.info(request, 'Username or Password is incorrect')
        return render(request, 'notes/login.html')

def signup(request):
    return render(request, 'notes/signup.html')

#@login_required(login_url='login')
def logout(request):
    logout(request)
    return redirect('login')

#@login_required(login_url='login')
def manage_account(request):
    return render(request, 'notes/manage_account.html')

#@login_required(login_url='login')
def notes_list(request):
    return render(request, 'notes/notes_list.html')

#@login_required(login_url='login')
def notes(request):
    return render(request, 'notes/notes.html')

#@login_required(login_url='login')
def create_notes(request):
    return render(request, 'notes/create_notes.html')

#@login_required(login_url='login')
def update_notes(request):
    return render(request, 'notes/update_notes.html')

#@login_required(login_url='login')
def delete_notes(request):
    pass