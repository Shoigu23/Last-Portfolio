from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from .filters import PostFilter
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

# Create your views here.

def home(request):
    if request.user.is_authenticated:
        username = request.user.first_name
        return render(request, 'home.html', {'username': username})
    else:
        return render(request, 'home.html')

def posts(request):
    posts = Post.objects.all()  # можно с галочками использовать
    myfilter = PostFilter(request.GET, queryset=posts)
    posts = myfilter.qs
    page = request.GET.get('page')
    paginator = Paginator(posts, 3)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {'posts': posts,'myfilter':myfilter}
    return render(request, 'posts.html', context) 

def post(request, id):
    post = Post.objects.get(id=id)
    context = {'post': post}
    return render(request, 'post.html', context) 

def profile(request):
    return render(request, 'profile.html') 

# create post
@login_required(login_url='home')
def createPost(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('posts')
    context = {'form':form}
    return render(request, 'post_form.html', context)

# update post
@login_required(login_url='home')
def updatePost(request, pk):
    post = Post.objects.get(id=pk)
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
        return redirect('posts')
    context = {'form':form}
    return render(request, 'post_form.html', context)

# delete post
@login_required(login_url="posts")
def deletePost(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('home')
    context = {'item':post}
    return render(request, 'delete.html', context)

@login_required(login_url='home')
def emailForm(request):
    return render(request, 'message.html')

@login_required(login_url='home')
def sendEmail(request):
    if request.method == 'POST':
        template = render_to_string('email_template.html', {
            'name':request.POST['name'],
            'email':request.POST['email'],
            'message':request.POST['message'],
        })
        email = EmailMessage(
            request.POST['subject'],
            template,
            settings.EMAIL_HOST_USER,
            ['toichubaev3930@mail.ru']
        )
        email.fail_silently=False
        email.send()
    return render(request, 'thanks.html')

def add_project(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'post_form.html', {'form': form})