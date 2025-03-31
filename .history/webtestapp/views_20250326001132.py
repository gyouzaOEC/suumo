from django.shortcuts import render
from .forms import DataForm

def index(request):
    my_dict = {
        "forms":DataForm(),
        ""
    }
    return render(request,"index.html",my_dict)
