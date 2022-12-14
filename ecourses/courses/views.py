from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.

def index(request):
    context = {
        'name':'THAI BAO'
    }
    return render(request, template_name='index.html', context = {
        'name':'Thai Bao'
    })

def welcome(request, year):
    return HttpResponse("HELLO " + str(year))

class TestView(View):
    def get(self, request):
        return HttpResponse("TESTING")

    def post(self, request):
        pass