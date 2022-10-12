from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from todolist.models import Task
from todolist.forms import taskForm
import datetime
from django.core import serializers

# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    todolist = Task.objects.filter(user=request.user)
    context = {
    'username': request.user.username,
    'data': todolist,
    }
    return render(request, "todolist.html", context)

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

def logout_user(request):
    logout(request)
    return redirect('todolist:login')

@login_required(login_url='/todolist/login/')
def create_task(request):
    form = taskForm(request.POST)
    if (form.is_valid() and request.method == 'POST'):
        title=form.cleaned_data["title"]
        description=form.cleaned_data["description"]
        date=datetime.datetime.now()
        user=request.user
        Task.objects.create(title=title, description=description, date=date, user=user)
        return redirect('todolist:show_todolist')
    form = taskForm()
    context = {'form':form}
    return render(request, 'create_task.html', context)

@login_required(login_url='/todolist/login/')
def status(request, id):
    task = Task.objects.get(id=id)
    task.is_finished = not(task.is_finished)
    task.save()
    return redirect('todolist:show_todolist')

@login_required(login_url='/todolist/login/')
def remove(request, id):
    Task.objects.get(id=id).delete()
    return redirect('todolist:show_todolist')

# TODOLIST AJAX
@login_required(login_url='/todolist/login/')
def todolist_ajax(request):
    ajax_todolist = Task.objects.filter(user=request.user)
    context = {
    'ajax_todolist' : ajax_todolist,
    'username' :  request.user.username,
    'last_login': request.COOKIES['last_login'],
    }
    return render(request, "todolist_ajax.html", context)

def show_json(request):
    data = Task.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data))

# CREATE TASK MODAL
def create_task_modal(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        date = datetime.datetime.now()
        user = request.user
        Task.objects.create(title=title, description=description, date=date, user=user)
         
        return HttpResponse(b"CREATED", status=201)