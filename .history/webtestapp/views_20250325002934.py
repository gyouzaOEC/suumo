from django.shortcuts import render


def index(request):
    return render(request,"webtestapp/templates/index.html")
