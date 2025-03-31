from django.shortcuts import render
from forms import dataForm

def index(request):
    
    return render(request,"index.html",)
