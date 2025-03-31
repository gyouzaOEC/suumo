from django.shortcuts import render
from forms import DataForm

def index(request):
    
    return render(request,"index.html",)
