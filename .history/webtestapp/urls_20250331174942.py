from django.urls import path
from . import views

app_name='webtestapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('result/', views.aaa, name='aaa'),
]

