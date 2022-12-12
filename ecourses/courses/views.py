from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    context = {
        'name':'THAI BAO'
    }
    return render(request, template_name='index.html', context = {
        'name':'Thai Bao'
    })