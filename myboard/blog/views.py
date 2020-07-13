from pyexpat import model
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone
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


