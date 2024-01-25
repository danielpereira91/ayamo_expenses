from django.shortcuts import render

def home(request):
    return render(request, template_name='home.html')

def contato(request):
    return HttpResponse('contato')

def sobre(request):
    return HttpResponse('sobre')
