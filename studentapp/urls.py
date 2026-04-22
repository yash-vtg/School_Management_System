from django.urls import path
from . import views

urlpatterns = [
    path('studentapp/',views.studenthome,name = 'studenthome'),
    path('studentbase/',views.studentbase,name = 'studentbase'),
    path('stuattend/',views.stuattend,name = 'stuattend'),
    path('stuslm/',views.stuslm,name = 'stuslm'),
    path('stulogout/',views.stulogout,name = 'stulogout'),
]