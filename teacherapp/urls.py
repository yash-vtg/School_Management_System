from django.urls import path
from . import views

#teacher app urls
urlpatterns = [
    path('teacherapp/',views.teacherhome,name='teacherhome'),
    path('teacherprofile/',views.teacherprofile,name='teacherprofile'),
    path('uploadpic/',views.uploadpic,name='uploadpic'),
    path('addattend/',views.addattend,name='addattend'),
    path('viewattendance/',views.viewattendance,name='viewattendance'),
    path('addslm/',views.addslm,name='addslm'),
    path('viewslm/',views.viewslm,name='viewslm'),
    path('tchangepass/',views.tchangepass,name='tchangepass'),
    path('teacherlogout/',views.teacherlogout,name='teacherlogout'),
    path('addstudent/',views.addstudent,name = 'addstudent'),
    path('viewstudent/',views.viewstudent,name = 'viewstudent'),
    path('editstu/<rollno>',views.editstu,name = 'editstu'),
    path('delstudent/<rollno>',views.delstudent,name = 'delstudent'),
]