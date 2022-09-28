from multiprocessing import context
from urllib import response
from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from todolist.forms import TodoList
from todolist.models import Task
from django.views.generic import CreateView


@login_required(login_url='/todolist/login/')
def show_todolist(request):
    todo = Task.objects.filter(user=request.user)
    context = {
        'list_todolist' : todo,
        'username' : request.user.username,
        'last_login': request.COOKIES['last_login'],
    }
    return render(request, "todolist.html", context)

# Create your views here.
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)


def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

def create_task(request):
    form = TodoList()
    if request.method == 'POST':
        form  = TodoList(request.POST)
        if form.is_valid():
            new_form = Task()
            new_form.user = request.user
            new_form.date = datetime.datetime.now()
            new_form.title = form.cleaned_data['title']
            new_form.description = form.cleaned_data['description']

            new_form.save()
            return redirect('todolist:show_todolist')
        else:
            # messages.info(request, 'Input tidak valid!')
            form = TodoList()
    context = {'form':form}
    return render(request, 'create_task.html', context)

def remove_task(request, id2):
    deletion = Task.objects.filter(id = id2)
    deletion.delete()
    return redirect(show_todolist)



        

