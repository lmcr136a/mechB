from pyexpat import model
from django.http import HttpResponse
from django.shortcuts import render
from .models import Post
from django.views.generic.dates import ArchiveIndexView, TodayArchiveView, YearArchiveView, MonthArchiveView, \
    DayArchiveView


# Create your views here.
def PostLV(request):
    return render(request,'templates/blog/post_list.html')

def PostDV(request):
    return render(request,'templates/blog/post_detail.html')

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


