from django.urls import path
from . import views

# maps urls to views

# url config
urlpatterns = [path("", views.home, name= "home")]
