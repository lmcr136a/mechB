from pyexpat import model
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from .forms import PostForm
from django.views.generic.dates import ArchiveIndexView, TodayArchiveView, YearArchiveView, MonthArchiveView, \
    DayArchiveView


# Create your views here.
def PostLV(request):
    posts=Post.objects.filter(pub_date__lte=timezone.now()).order_by('pub_date')
    return render(request,'templates/blog/post_list.html',{'posts':posts})

def PostDV(request, pk):
    post = get_object_or_404(Post, pk = pk)
    return render(request,'templates/blog/post_detail.html', {'post':post})

def PostAV(request):
    return render(request,'templates/blog/post_list.html')
def PostYAV(request):
    return render(request,'templates/blog/post_list.html')
def PostMAV(request):
    return render(request,'templates/blog/post_list.html')
def PostDAV(request):
    return render(request,'templates/blog/post_list.html')
def PostTAV(request):
    return render(request,'templates/blog/post_list.html')
def PostN(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
        return redirect('PostDV', pk=post.pk)
    else:
        form = PostForm
    return render(request,'blog/post_edit.html',{'form':form})

def PostE(request,pk):
    post=get_object_or_404(Post,pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST,instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.mod_date=timezone.now()
            post.save()
            return redirect('blog:PostDV', pk=post.pk)
    else:
        form=PostForm(instance=post)
    return render(request,'blog/post_edit.html', {'form':form})

