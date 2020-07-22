from django.shortcuts import render, get_object_or_404, redirect
from .models import Fost
from django.urls import reverse
from django.utils import timezone
from .forms import FostForm
from django.views import generic
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect, HttpResponse

import urllib
import os
import mimetypes
#from somewhere import handle_uploaded_file
# Create your views here.


def genealogy_list(request):
    genealogys=Fost.objects.filter(pub_date__lte=timezone.now()).order_by('pub_date')
    return render(request,'html/genealogy_list.html',{'genealogys':genealogys})


def genealogy_detail(request, pk):
    genealogy = get_object_or_404(Fost, pk = pk)
    return render(request,'html/genealogy_detail.html', {'genealogy':genealogy})


def upload_genealogy(request):
    form = FostForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            genealogy = form.save(commit=False)
            genealogy.author = request.user
            genealogy.pub_date = timezone.now()
            if 'file' in request.FILES.keys():
                genealogy.filename = request.FILES['file'].name
            genealogy.save()
            form.save()
            return redirect('genealogy:genealogy_list')
    return render(request, 'html/edit_genealogy.html', {'form': form})


def edit_genealogy(request,pk):
    genealogy=get_object_or_404(Fost,pk=pk)
    if request.method == "POST":
        form = FostForm(request.POST,instance=genealogy)
        if form.is_valid():
            if genealogy.author == request.user:
                genealogy = form.save(commit=False)
                genealogy.mod_date=timezone.now()
                if 'file' in request.FILES.keys():
                    genealogy.filename = request.FILES['file'].name
                genealogy.save()
            return redirect('genealogy:genealogy_detail', pk=genealogy.pk)
        else: render(request, 'html/author_error.html',{})
    else:
        form=FostForm(instance=genealogy)
    return render(request,'html/edit_genealogy.html', {'form':form})


def delete_genealogy(request, genealogy_id=None):
    genealogy_to_delete=Fost.objects.get(id=genealogy_id)
    genealogy_to_delete.delete()
    return redirect('genealogy:genealogy_list')


def download_genealogy(request, pk):
    genealogy = get_object_or_404(Fost, pk=pk)
    url = genealogy.file.url

    if os.path.exists(url):
        with open(url, 'rb') as fh:
            quote_file_url = urllib.parse.quote(genealogy.filename.encode('utf-8'))
            response = HttpResponse(fh.read(), content_type=mimetypes.guess_type(url)[0])
            response['Content-Disposition'] = 'attachment;filename*=UTF-8\'\'%s' % quote_file_url
            return response
    return HttpResponse('Cant find files url')





## inline이면 파일을 웹 브라우저 내에서 볼 수 있고, attachment이면 파일을 내려받을 수 있다.
## disposition-parm인 filename은 파일을 내려받을 때 파일 이름을 지정한다.




