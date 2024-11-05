from django.urls import path
from . import views

# maps urls to views

# url config
urlpatterns = [
    path('hello/', views.say_hello)
]