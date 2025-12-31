from django.contrib import admin
from django.urls import path,include
from . import views

#Create urls on here..

urlpatterns = [
    path('adminhome/',views.adminhome,name = 'adminhome'),
    path('viewenquiry/',views.viewenquiry,name = 'viewenquiry'),
    path('addclass/',views.addclass,name = 'addclass'),
    path('viewclass/',views.viewclass,name = 'viewclass'),
    path('adminlogout/',views.adminlogout,name = 'adminlogout'),
    path('addsubjects/',views.addsubjects,name = 'addsubjects'),
    path('viewsubjects/',views.viewsubjects,name = 'viewsubjects'),
    path('delenq/<id>',views.delenq,name = 'delenq'),
    path('editclass/<id>',views.editclass,name = 'editclass'),
    path('delclass/<cid>',views.delclass,name = 'delclass'),
    path('addstudent/',views.addstudent,name = 'addstudent'),
    path('viewstudent/',views.viewstudent,name = 'viewstudent'),
    path('editsubject/<id>',views.editsubject,name = 'editsubject'),
    path('addteacher/',views.addteacher,name = 'addteacher'),
    path('viewteacher/',views.viewteacher,name = 'viewteacher'),
    path('delteacher/<id>',views.delteacher,name = 'delteacher'),
    path('editteacher/<id>',views.editteacher,name = 'editteacher'),
    path('editstu/<rollno>',views.editstu,name = 'editstu'),
    path('addnoti/',views.addnoti,name = 'addnoti'),
    path('viewnoti/',views.viewnoti,name = 'viewnoti'),
    path('delsub/<sid>',views.delsub,name = 'delsub'),
    path('delstudent/<rollno>',views.delstudent,name = 'delstudent'),
]
