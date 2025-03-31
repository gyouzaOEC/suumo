from django.shortcuts import render
from forms import DataForm

def index(request):
    my_dict = {
        "form"
    }
    return render(request,"index.html",)
