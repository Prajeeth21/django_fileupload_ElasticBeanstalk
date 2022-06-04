import imp
from django.shortcuts import render, HttpResponse

from .forms import MyfileUploadForm

# Create your views here.
def index(request):
    context = {
        'form': MyfileUploadForm()
    }
    return render(request, 'index.html', context)
