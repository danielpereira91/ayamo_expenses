from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('add_expense/', views.add_expense),

]    