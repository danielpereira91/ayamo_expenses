from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, template_name='ayamo_refunds/pages/home.html')

def contato(request):
    return HttpResponse('contato')

def sobre(request):
    return HttpResponse('sobre')
