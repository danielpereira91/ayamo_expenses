from django.shortcuts import render

def home(request):
    return render(request, 'ayamo_refunds/pages/home.html')

def contato(request, id):
    return render(request, 'ayamo_refunds/pages/expense-view.html')
