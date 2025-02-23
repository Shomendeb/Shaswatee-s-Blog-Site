from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages

from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class CustomPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'registration/password_change.html'
    success_url = reverse_lazy('password_change_done')

def password_change_done(request):
    return render(request, 'registration/password_change_done.html')

def post_list(request):
    posts = Post.objects.all()

    #posts = Post.objects.filter(owner=request.user).order_by("-created_date") # Task.objects.filter(user=request.user).order_by("-created_at")

    return render(
        request,
        "blog/post_list.html",
        {"posts": posts},
    )

@login_required
def myposts(request):
    
    posts = Post.objects.filter(owner=request.user).order_by("-created_date") 

    return render(
        request,
        "blog/post_list.html",
        {"posts": posts},
    )
    

def post_details(request, id):
    post = get_object_or_404(Post, id=id)
    
    return render(request, "blog/post_details.html", {'post':post})

@login_required
def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.owner = request.user
            post.save()
            messages.success(request, 'Post created successfully.')
            return redirect("post_list")
    else:
        form = PostForm()
    return render(request, "blog/post_create.html", {"form": form})

@login_required
def post_update(request, id):
    post = get_object_or_404(Post, id=id)
    
    if request.user != post.owner:
        messages.error(request, 'You do not have permission to update this post.')
        return redirect('post_details', id=post.id)
    if request.method=='POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post updated successfully.')
            return redirect('post_list')
    else:
        form = PostForm(instance=post)
    return render(request, "blog/post_create.html", {"form": form})

@login_required
def post_detele(request, id):
    post = get_object_or_404(Post, id=id)
    if request.user != post.owner:
        messages.error(request, 'You do not have permission to delete this post.')
        return redirect('post_details', id=post.id)
    post.delete()
    messages.success(request, 'Post deleted successfully.')
    return redirect('post_list')

def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("post_list")
    else:
        form = UserCreationForm()

    return render(request, "registration/signup.html", {"form": form})