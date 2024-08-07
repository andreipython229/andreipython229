from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    return render(request, 'index.html')


def andrzej(request):
    return request('/')

@csrf_exempt
def andrej2(request):
        return render(request, 'andrzej.html',{'name': 'andrzej','age':51, 'state':very_good})
