from django.urls import path
from . views import *



urlpatterns=[
    path('',index,name='index'),
    path('about/',about,name='about'),
    path('VM/',VM,name='VM'),
    path('contact/',contact,name='contact'),
    path('login/',login,name='login'),
    path('logcode/',logcode,name='logcode'),
    path('founder/',founder,name='founder'),
    path('chairman/',chairman,name='chairman'),
    path('princi/',princi,name='princi'),
    path('smteam/',smteam,name='smteam'),
]

