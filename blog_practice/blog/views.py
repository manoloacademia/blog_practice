from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from matplotlib.style import context
from .models import Post
from .forms import PostForm, CreateUserForm
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def home(request):
    return render(request, 'home.html', {})

@login_required(login_url='login')
def about(request):
    return render(request, 'about.html', {})

@login_required(login_url='login')
def pages(request):
    text_list = Post.objects.all()
    context = {'text_list': text_list}
    return render(request, 'pages.html', context)

@login_required(login_url='login')
def page_detail(request, pk):
    page_detail = Post.objects.get(pk=pk)
    context = {'post': page_detail}
    return render(request, 'page_detail.html', context)

@login_required(login_url='login')
def page_create(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'page_create.html', context)

@login_required(login_url='login')
def page_update(request, pk):
    page = Post.objects.get(pk=pk)
    form = PostForm(instance=page) # this allows to check for the pk object
    if request.method == 'POST':
        form = PostForm(request.POST, instance=page)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'post': form}
    return render(request, 'page_update.html', context)

@login_required(login_url='login')
def page_delete(request, pk):
    page_delete = Post.objects.get(pk=pk)
    if request.method == 'POST':
        page_delete.delete()
        return redirect('/')
    context = {'delete_post': page_delete}
    return render(request,'page_delete.html', context)

def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('login')
        context = {'form': form}
        return render(request, 'register.html', context)

def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username or Password is incorrect.')
                
        context = {}
        return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect('login')