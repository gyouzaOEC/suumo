from django.shortcuts import render
from forms.py import DataForm

def index(request):
    my_dict = {
        "form":DataForm(),
    }
    return render(request,"index.html",my_dict)
