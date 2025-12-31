from django.shortcuts import *
from adminapp.models import *
from . models import *
from django.core.files.storage import FileSystemStorage
from django.views.decorators.cache import cache_control

# Create your views here.
@cache_control(no_store = True,no_cache = True,must_revalidate = True)
def teacherhome(req):
  try:   
    if req.session['teacherid']!=None:
      teacherid = req.session['teacherid']
      stu_count = Student.objects.all().count()
      ccount = Classes.objects.all().count()
      atten = Attendence.objects.all().count()
      sub = Subject.objects.all().count()
      teacher = Teacher.objects.get(emailaddress=teacherid)
      return render(req,'teacherhome.html',{'teacher':teacher,'stu_count':stu_count,'ccount':ccount,'atten':atten,'sub':sub})
  except KeyError:
    return redirect('login')    

@cache_control(no_store = True,no_cache = True,must_revalidate = True)
def teacherprofile(req):
    try:   
        if req.session['teacherid']!=None:
            teacherid = req.session['teacherid']
            teacher = Teacher.objects.get(emailaddress=teacherid)
            if req.method == "POST":
              name = req.POST['name']
              fname = req.POST['fname']
              mname = req.POST['mname']
              gender = req.POST['gender']
              dob = req.POST['dob']
              contactno = req.POST['contactno']
              address = req.POST['address']
              qualification = req.POST['qualification']
              tl = Teacher.objects.filter(emailaddress=teacherid).update(name=name,fname=fname,mname=mname,gender=gender,dob=dob,contactno=contactno,address=address,qualification=qualification)
              return redirect ('teacherapp:teacherprofile')
            return render(req,'teacherprofile.html',{'teacher':teacher})
    except KeyError:
        return redirect('login')

@cache_control(no_store = True,no_cache = True,must_revalidate = True)
def uploadpic(req):
   if req.method == "POST":
      teacherid = req.session['teacherid']
      teacher = Teacher.objects.get(emailaddress=teacherid)
      pic = req.FILES['pic']
      fs = FileSystemStorage()
      filename = fs.save(pic.name,pic)
      teacher.pic = filename
      teacher.save()
      return redirect('teacherapp:teacherprofile')


@cache_control(no_store = True,no_cache = True,must_revalidate = True)
def addattend(req):
    try:
      if req.session['teacherid']!=None:
        teacherid = req.session['teacherid']
        teacher = Teacher.objects.get(emailaddress=teacherid)
        st = Student.objects.filter(sclass=teacher.tclass)
        if req.method == "POST":
           sid = req.POST['sid']
           rollno = req.POST['rollno']
           name = req.POST['name']
           status = req.POST['status']
           created_date = req.POST['created_date']
           att = Attendence(sid=sid,rollno=rollno,sclass=teacher.tclass,tclass=teacher.tclass,name=name,status=status,created_date=created_date)
           att.save()
           return redirect('teacherapp:addattend')
        return render(req,'addattend.html',{'teacher':teacher,'st':st})
    except KeyError:
       return redirect('login')

@cache_control(no_store = True,no_cache = True,must_revalidate = True)
def viewattendance(req):
    try:
      if req.session['teacherid']!=None:
        teacherid = req.session['teacherid']
        teacher = Teacher.objects.get(emailaddress=teacherid)
        att = Attendence.objects.filter(sclass = teacher.tclass)
        return render(req,'viewattendance.html',{'teacher':teacher,'att':att})
    except KeyError:
       return redirect('login')

@cache_control(no_store = True,no_cache = True,must_revalidate = True)
def addslm(req):
    try:
      if req.session['teacherid']!=None:
        teacherid = req.session['teacherid']
        teacher = Teacher.objects.get(emailaddress=teacherid)
        if req.method == "POST":
           title = req.POST['title']
           sm = req.FILES['sm']
           slm = StudyMaterial(title=title,sm=sm,tclass=teacher.tclass)
           slm.save()
           return redirect('teacherapp:viewslm')
        return render(req,'addslm.html',{'teacher':teacher})
    except KeyError:
       return redirect('login')

@cache_control(no_store = True,no_cache = True,must_revalidate = True)
def viewslm(req):
    try:
      if req.session['teacherid']!=None:
        teacherid = req.session['teacherid']
        teacher = Teacher.objects.get(emailaddress=teacherid)
        return render(req,'viewslm.html',{'teacher':teacher})
    except KeyError:
       return redirect('login')
    
@cache_control(no_store = True,no_cache = True,must_revalidate = True)
def teacherlogout(req):
    try:
      if req.session['teacherid']!=None:
        del req.session['teacherid']
        return redirect('login')
    except KeyError:
      return redirect('login')

@cache_control(no_store = True,no_cache = True,must_revalidate = True)
def tchangepass(req):
    try:
      if req.session['teacherid']!=None:
        teacherid = req.session['teacherid']
        teacher = Teacher.objects.get(emailaddress=teacherid)
        if req.method=="POST":
           oldpassword = req.POST['oldpassword']
           newpassword = req.POST['newpassword']
           cnfpassword = req.POST['cnfpassword']
           if newpassword != cnfpassword:
              msg = "Both password did not match"
              return render(req,'tchangepass.html',{'msg':msg})
           elif teacher.password != oldpassword:
              msg = "Enter Correct old Password"
              return render(req,'tchangepass.html',{'msg':msg})
           elif teacher.password == oldpassword:
              Teacher.objects.filter(emailaddress = teacherid).update(password = newpassword)
              return redirect('teacherapp:teacherlogout')
        return render(req,'tchangepass.html',{'teacher':teacher})
    except KeyError:
       return redirect('login')
