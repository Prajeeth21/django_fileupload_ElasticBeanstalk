import imp
from urllib import request
from django.shortcuts import render, HttpResponse

from .forms import MyfileUploadForm
from .models import file_upload

# Create your views here.
def index(request):

    if request.method == "POST":
        form = MyfileUploadForm(request.POST, request.FILES)
        print(form.as_p)
        if form.is_valid():
            name = form.cleaned_data['file_name']
            the_files = form.cleaned_data['files_data']
            #file_upload(file_name= name, my_file = files).save()
            return HttpResponse("File uploaded")
        else:
            return HttpResponse("Error")

    else:
        context = {
            'form': MyfileUploadForm()
        }
        return render(request, 'index.html', context)
