from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

def index(request):
    tasks = Post.objects.all()
    return render(request, 'swap/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})

def about(request):
    return render(request, 'swap/about.html')

def create(request):
    error = ''
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'

    form = PostForm()
    context = {
        'form': form,
        'error': error,
    }
    return render(request, 'swap/create.html', context)
