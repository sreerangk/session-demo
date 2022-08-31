from django.urls import path
from  . import views


urlpatterns = [
    path('',viwes.home, name='home')
]