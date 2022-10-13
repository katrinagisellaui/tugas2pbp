from hashlib import new
from multiprocessing import context
from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
import todolist
from todolist.forms import TodoList
from todolist.models import Task
from django.http import JsonResponse, HttpResponse, HttpResponseNotFound
from django.core import serializers


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
            response.set_cookie('last_login', str(datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
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

@login_required(login_url='/todolist/login/')
def create_task(request):
    form = TodoList()
    if request.method == "POST":
        form = TodoList(request.POST)
        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save() 
            return redirect('todolist:show_todolist')
    
    context = {'form':form}
    return render(request, 'create_task.html', context)

@login_required(login_url='/todolist/login/')
def get_todolist_json(request):
    todolist_item = Task.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", todolist_item), content_type="application/json")

@login_required(login_url='/todolist/login/')
def add_todolist_item(request):
    if request.method == 'POST':
        task_title = request.POST.get("title")
        task_description = request.POST.get("description")
        user = request.user
        date = datetime.now()
        is_finished = False
        new_task = Task(user=user, date=date, title=task_title, description=task_description, is_finished=is_finished)
        new_task.save()
        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()


def remove_task(request, id):
    deletion = Task.objects.filter(id=id)
    deletion.delete()
    return redirect('todolist:show_todolist')

def change_done(request, id):
    change = Task.objects.get(id = id)
    change.is_finished = not(change.is_finished)
    change.save()
    return redirect('todolist:show_todolist')



        

