from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from .forms import PostForm

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def about(request):
    return HttpResponse('This is the about page, from myself.')

def pages(request):
    text_list = Post.objects.all()
    context = {'text_list': text_list}
    return render(request, 'pages.html', context)

def page_detail(request, pk):
    page_detail = Post.objects.get(pk=pk)
    context = {'post': page_detail}
    return render(request, 'page_detail.html', context)

def page_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/') # This is an example from https://docs.djangoproject.com/en/4.0/topics/forms/
    else:
        form = PostForm()
    return render(request, 'page_create.html', {'form': form})