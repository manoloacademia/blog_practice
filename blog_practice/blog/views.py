from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from .models import Post
from .forms import PostForm
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def about(request):
    return render(request, 'about.html', {})

def pages(request):
    text_list = Post.objects.all()
    context = {'text_list': text_list}
    return render(request, 'pages.html', context)

def page_detail(request, pk):
    page_detail = Post.objects.get(pk=pk)
    context = {'post': page_detail}
    return render(request, 'page_detail.html', context)

def page_create(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'page_create.html', context)

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

def page_delete(request, pk):
    page_delete = Post.objects.get(pk=pk)
    if request.method == 'POST':
        page_delete.delete()
        return redirect('/')
    context = {'delete_post': page_delete}
    return render(request,'page_delete.html', context)

def register(request):
    form = UserCreationForm()
    context = {'form': form}
    return render(request, 'register.html', context)

def login(request):
    context = {}
    return render(request, 'login.html', context)