from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('welcome/<int:year>', views.welcome, name="welcome"),
    path('test/', views.TestView.as_view()),
]