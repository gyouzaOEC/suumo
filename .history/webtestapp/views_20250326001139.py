from django.shortcuts import render
from .forms import DataForm

def index(request):
    my_dict = {
        "forms":DataForm(),
        "price":0
    }
    return render(request,"index.html",my_dict)
