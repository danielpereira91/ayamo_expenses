from django.shortcuts import render

def home(request):
    return render(request, 'ayamo_refunds/pages/home.html')

def add_expense(request):
    return render(request, 'ayamo_refunds/pages/add_expense.html')
