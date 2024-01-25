from django.urls import path
from ayamo_refunds.views import home, contato, sobre

urlpatterns = [
    path('', home),
    path('contato/', contato),
    path('sobre/', sobre),
]    