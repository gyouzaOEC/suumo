from django.shortcuts import render
from .forms import DataForm

def index(request):
    my_dict = {
        "forms":DataForm(),
        "price":
    }
    return render(request,"index.html",my_dict)
