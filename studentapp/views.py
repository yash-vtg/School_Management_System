from django.shortcuts import render,redirect
from django.views.decorators.cache import cache_control
from adminapp.models import *
from teacherapp.models import *

# Create your views here.
@cache_control(no_store = True,no_cache = True,must_revalidate = True)
def studenthome(req):
    try:
      if req.session['studentid']!=None:
        studentid = req.session['studentid']
        stu_count = Student.objects.all().count()
        sub = Subject.objects.all().count()
        student = Student.objects.get(emailaddress=studentid)
        return render(req,'studenthome.html',{'student':student,'stu_count':stu_count,'sub':sub})
    except KeyError:
       return redirect('login')
    
@cache_control(no_store = True,no_cache = True,must_revalidate = True)
def studentbase(req):
    try:
      if req.session['studentid']!=None:
        studentid = req.session['studentid']
        return render(req,'studentbase.html',{'studentid':studentid})
    except KeyError:
       return redirect('login')
    
@cache_control(no_store = True,no_cache = True,must_revalidate = True)
def stuattend(req):
    try:
      if req.session['studentid']!=None:
        studentid = req.session['studentid']
        student = Student.objects.get(emailaddress=studentid)
        att = Attendence.objects.filter(rollno=student.rollno)
        return render(req,'stuattend.html',{'student':student,'att':att})
    except KeyError:
       return redirect('login')
    
@cache_control(no_store = True,no_cache = True,must_revalidate = True)
def stuslm(req):
    try:
      if req.session['studentid']!=None:
        studentid = req.session['studentid']
        student = Student.objects.get(emailaddress=studentid)
        slm = StudyMaterial.objects.filter(tclass=student.sclass)
        return render(req,'stuslm.html',{'student':student,'slm':slm})
    except KeyError:
       return redirect('login')

@cache_control(no_store = True,no_cache = True,must_revalidate = True)
def stulogout(req):
    try:
      if req.session['studentid']!=None:
        del req.session['studentid']
        return redirect('login')
    except KeyError:
      return redirect('login')