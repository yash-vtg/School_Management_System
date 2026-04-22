from django.contrib import admin
from django.urls import path,include
from . import views

#Create urls on here..

urlpatterns = [
    path('adminhome/',views.adminhome,name = 'adminhome'),
    path('adminlogout/',views.adminlogout,name = 'adminlogout'),
    path('viewenquiry/',views.viewenquiry,name = 'viewenquiry'),
    path('delenq/<id>',views.delenq,name = 'delenq'),
    path('addclass/',views.addclass,name = 'addclass'),
    path('viewclass/',views.viewclass,name = 'viewclass'),
    path('editclass/<id>',views.editclass,name = 'editclass'),
    path('delclass/<cid>',views.delclass,name = 'delclass'),
    path('addsubjects/',views.addsubjects,name = 'addsubjects'),
    path('viewsubjects/',views.viewsubjects,name = 'viewsubjects'),
    path('editsubject/<id>',views.editsubject,name = 'editsubject'),
    path('delsub/<sid>',views.delsub,name = 'delsub'),
    path('addstudent/',views.addstudent,name = 'addstudent'),
    path('viewstudent/',views.viewstudent,name = 'viewstudent'),
    path('editstu/<rollno>',views.editstu,name = 'editstu'),
    path('delstudent/<rollno>',views.delstudent,name = 'delstudent'),
    path('addteacher/',views.addteacher,name = 'addteacher'),
    path('viewteacher/',views.viewteacher,name = 'viewteacher'),
    path('delteacher/<id>',views.delteacher,name = 'delteacher'),
    path('editteacher/<id>',views.editteacher,name = 'editteacher'),
    path('addnoti/',views.addnoti,name = 'addnoti'),
    path('viewnoti/',views.viewnoti,name = 'viewnoti'),
]
