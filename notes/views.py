from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from notes.forms import CustomUserForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from notes.models import Note
from django.contrib.auth.forms import PasswordChangeForm

def index(request):
    return render(request, 'notes/index.html')

@csrf_exempt
def login_user(request):
    if request.user.is_authenticated:
        return redirect('/notes_list')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user     = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('notes:notes_list')
            else:
                messages.info(request, 'Username or Password is incorrect')
        return render(request, 'notes/login.html')

def signup(request):
    if request.method != 'POST':
        form = CustomUserForm()
    else:
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notes:login_user')
        else:
            messages.error(request, 'Error in system')

    context = {'form': form}
    return render(request, 'notes/signup.html', context)

@login_required(login_url='/login')
def logout_user(request):
    logout(request)
    return redirect('notes:login_user')

@login_required(login_url='/login')
def manage_account(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your password was successfully updated!')
            return redirect('notes:notes_list')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(user=request.user)

    return render(request, 'notes/manage_account.html', {'form': form})

@login_required(login_url='/login')
def notes_list(request):
    user_id     = request.user.id
    user        = User.objects.get(pk=user_id)
    if user is not None:
        list_note   = Note.objects.filter(writter = user)
        context = {
            'list_note': list_note,
        }
        return render(request, 'notes/notes_list.html', context=context)
    else:
        messages.info(request, 'Error in system')
    return render(request, 'notes/notes_list.html')

@login_required(login_url='/login')
def notes(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    context = {
        'note': note,
    }
    return render(request, 'notes/notes.html', context)

@login_required(login_url='/login')
def create_notes(request):
    if request.method == 'POST':
        user_id = request.user.id
        user = User.objects.get(pk=user_id)
        title = request.POST.get('title')
        body = request.POST.get('body')

        if user is not None:
            note = Note(note_title=title, note_body=body, writter=user)
            note.save()
            messages.success(request, 'Successfully create the Note.')
            return redirect('notes:notes_list')  
        else:
            messages.error(request, 'Error in system')
    
    return render(request, 'notes/create_notes.html')

@login_required(login_url='/login')
def update_notes(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    context = {
        'note': note,
    }
    if request.method == 'POST':
        note.note_title = request.POST.get('title')
        note.note_body = request.POST.get('body')
        note.save()
        messages.success(request, 'Note successfully updated.')
        return redirect('notes:notes_list')
    return render(request, 'notes/update_notes.html', context)

@login_required(login_url='/login')
def delete_notes(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    note.delete()
    messages.success(request, 'Note successfully deleted.')
    return redirect('notes:notes_list')