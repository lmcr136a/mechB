from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.urls import reverse
from django.utils import timezone
from .forms import PostForm
from django.views import generic
# Create your views here.

def post_list(request):
    posts=Post.objects.filter(pub_date__lte=timezone.now()).order_by('pub_date')
    return render(request,'html/post_list.html',{'posts':posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk = pk)
    return render(request,'html/post_detail.html', {'post':post})

def new_post(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        post = form.save(commit=False)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.pub_date = timezone.now()
            post.save()
        return redirect('board:post_list')
    else:
        form = PostForm
    return render(request,'html/edit_post.html',{'form':form})

def edit_post(request,pk):
    post=get_object_or_404(Post,pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST,instance=post)
        if form.is_valid():
            if post.author == request.user:
                post = form.save(commit=False)
                post.mod_date=timezone.now()
                post.save()
            return redirect('board:post_detail', pk=post.pk)
        else: render(request, 'html/author_error.html',{})
    else:
        form=PostForm(instance=post)
    return render(request,'html/edit_post.html', {'form':form})

def delete_post(request, post_id=None):
    post_to_delete=Post.objects.get(id=post_id)
    post_to_delete.delete()
    return redirect('board:post_list')

