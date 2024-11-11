from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


# Test View
def say_hello(request):
    return render(request, "Page.html")
