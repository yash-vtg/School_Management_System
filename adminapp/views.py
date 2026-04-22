from django.shortcuts import render,redirect
from smsapp.models import Enquiry
from django.utils import timezone 
from . models import *
from django.views.decorators.cache import cache_control
import datetime


# Create your views here.


@cache_control(no_store = True,no_cache = True,must_revalidate = True)
def adminhome(req):
    try:
      if req.session['adminid']!=None:
        adminid = req.session['adminid']
        stu_count = Student.objects.all().count()
        tea_count = Teacher.objects.all().count()
        ccount = Classes.objects.all().count()
        atten = Attendence.objects.all().count()
        sub = Subject.objects.all().count()
        notification = Notification.objects.all().count()
        return render(req,'adminhome.html',{'adminid':adminid,'stu_count':stu_count,'tea_count':tea_count,'ccount':ccount,'atten':atten,'sub':sub,'notification':notification})
    except KeyError:
       return redirect('login')
      
@cache_control(no_store = True,no_cache = True,must_revalidate = True)
def viewenquiry(req):
    try:
      if req.session['adminid']!=None:
        adminid = req.session['adminid']
        enq = Enquiry.objects.all()
        return render(req,'viewenquiry.html',{'adminid':adminid,'enq':enq})
    except KeyError:
       return redirect('login')

@cache_control(no_store = True,no_cache = True,must_revalidate = True)    
def addclass(req):
    try:
      if req.session['adminid']!=None:
        adminid = req.session['adminid']
        if req.method == "POST":
          class_name = req.POST['class_name']
          seats = req.POST['seats']
          roomno = req.POST['roomno']
          created_date = timezone.now()
          cl = Classes(class_name = class_name,seats = seats,roomno = roomno,created_date = created_date)
          cl.save()
          return redirect('adminapp:viewclass')
        return render(req,'addclass.html',{'adminid':adminid})
    except KeyError:
       return redirect('login')

@cache_control(no_store = True,no_cache = True,must_revalidate = True)    
def viewclass(req):
    try:
      if req.session['adminid']!=None:
        adminid = req.session['adminid']
        cl = Classes.objects.all()
        return render(req,'viewclass.html',{'adminid':adminid,'cl':cl})
    except KeyError:
       return redirect('login')

@cache_control(no_store = True,no_cache = True,must_revalidate = True)
def editclass(req,id):
    try:
      if req.session['adminid']!=None:
        adminid = req.session['adminid']
        cl = Classes.objects.get(cid=id)
        if req.method == 'POST':
           class_name = req.POST['class_name']
           seats = req.POST['seats']
           roomno = req.POST['roomno']
           Classes.objects.filter(cid=id).update(class_name=class_name,seats=seats,roomno=roomno)
           return redirect('adminapp:viewclass')
        return render(req,'editclass.html',{'adminid':adminid,'cl':cl})
    except KeyError:
       return redirect('login')

def delclass(req,cid):
    try:
      if req.session['adminid']!=None:
         Classes.objects.get(cid=cid).delete()
         return redirect('adminapp:viewclass')
    except KeyError:
       return redirect('login')

@cache_control(no_store = True,no_cache = True,must_revalidate = True)
def adminlogout(req):
    try:
      if req.session['adminid']!=None:
        del req.session['adminid']
        return redirect('login')
    except KeyError:
      return redirect('login')
    
@cache_control(no_store = True,no_cache = True,must_revalidate = True)    
def addsubjects(req):
    try:
      if req.session['adminid']!=None:
        adminid = req.session['adminid']
        cl = Classes.objects.all()
        if req.method == "POST":
          subject_name = req.POST['subject_name']
          book = req.POST['book']
          steacher = req.POST['steacher']
          created_date = timezone.now()
          sl = Subject(subject_name = subject_name,book = book,steacher = steacher,created_date = created_date)
          sl.save()
          return redirect('adminapp:viewsubjects')
        return render(req,'addsubjects.html',{'adminid':adminid,'cl':cl})
    except KeyError:
       return redirect('login')

@cache_control(no_store = True,no_cache = True,must_revalidate = True)    
def viewsubjects(req):
    try:
      if req.session['adminid']!=None:
        adminid = req.session['adminid']
        sl = Subject.objects.all()
        return render(req,'viewsubjects.html',{'adminid':adminid,'sl':sl})
    except KeyError:
       return redirect('login')
     
@cache_control(no_store = True,no_cache = True,must_revalidate = True)
def editsubject(req,id):
    try:
      if req.session['adminid']!=None:
        adminid = req.session['adminid']
        sl = Subject.objects.get(sid=id)
        if req.method == 'POST':
           subject_name = req.POST['subject_name']
           sclass = req.POST['sclass']
           book = req.POST['book']
           steacher = req.POST['steacher']
           Subject.objects.filter(sid=id).update(subject_name=subject_name,sclass=sclass,book=book,steacher=steacher)
           return redirect('adminapp:viewsubjects')
        return render(req,'editsubject.html',{'adminid':adminid,'sl':sl})
    except KeyError:
       return redirect('login')
    
def delsub(req,sid):
    try:
      if req.session['adminid']!=None:
         Subject.objects.get(sid=sid).delete()
         return redirect('adminapp:viewsubjects')
    except KeyError:
       return redirect('login')
    
def delenq(req,id):
    try:
      if req.session['adminid']!=None:
         Enquiry.objects.get(id=id).delete()
         return redirect('adminapp:viewenquiry')
    except KeyError:
       return redirect('login')
    
    
@cache_control(no_store = True,no_cache = True,must_revalidate = True)
def addstudent(req):
    try:
      if req.session['adminid']!=None:
        adminid = req.session['adminid']
        cl = Classes.objects.all()
        if req.method == "POST":
          rollno = req.POST['rollno']
          name = req.POST['name']
          fname = req.POST['fname']
          mname = req.POST['mname']
          gender = req.POST['gender']
          dob = req.POST['dob']
          contactno = req.POST['contactno']
          emailaddress = req.POST['emailaddress']
          address = req.POST['address']
          sclass = req.POST['sclass']
          feespaid = req.POST['feespaid']
          duefees = req.POST['duefees']
          created_date = timezone.now()
          stul = Student(rollno=rollno,name=name,fname=fname,mname=mname,gender=gender,dob=dob,contactno=contactno,emailaddress=emailaddress,address=address,sclass=sclass,feespaid=feespaid,duefees=duefees,password="54321",created_date=created_date)
          stul.save()
          return redirect('adminapp:viewstudent')
        return render(req,'addstudent.html',{'adminid':adminid,'cl':cl})
    except KeyError:
       return redirect('login')

@cache_control(no_store = True,no_cache = True,must_revalidate = True)
def viewstudent(req):
    try:
      if req.session['adminid']!=None:
        adminid = req.session['adminid']
        stul = Student.objects.all()
        return render(req,'viewstudent.html',{'adminid':adminid,'stul':stul})
    except KeyError:
       return redirect('login')
     
@cache_control(no_store = True,no_cache = True,must_revalidate = True)
def editstu(req,rollno):
    try:
      if req.session['adminid']!=None:
        adminid = req.session['adminid']
        cl = Classes.objects.all()
        stul = Student.objects.get(rollno=rollno)
        if req.method == 'POST':
          rollno = req.POST['rollno']
          name = req.POST['name']
          fname = req.POST['fname']
          mname = req.POST['mname']
          gender = req.POST['gender']
          dob = req.POST['dob']
          contactno = req.POST['contactno']
          emailaddress = req.POST['emailaddress']
          address = req.POST['address']
          sclass = req.POST['sclass']
          feespaid = req.POST['feespaid']
          duefees = req.POST['duefees']
          created_date = timezone.now()
          Student.objects.filter(rollno=rollno).update(rollno=rollno,name=name,fname=fname,mname=mname,gender=gender,dob=dob,contactno=contactno,emailaddress=emailaddress,address=address,sclass=sclass,feespaid=feespaid,duefees=duefees,password="54321",created_date=created_date)
          return redirect('adminapp:viewstudent')
        return render(req,'editstu.html',{'adminid':adminid,'stul':stul,'cl':cl})
    except KeyError:
       return redirect('login')
    
def delstudent(req,rollno):
    try:
      if req.session['adminid']!=None:
         Student.objects.get(rollno=rollno).delete()
         return redirect('adminapp:viewstudent')
    except KeyError:
       return redirect('login')

@cache_control(no_store = True,no_cache = True,must_revalidate = True)
def addteacher(req):
    try:
      if req.session['adminid']!=None:
        adminid = req.session['adminid']
        cl = Classes.objects.all()
        if req.method == "POST":
          name = req.POST['name']
          pic = req.POST['pic']
          fname = req.POST['fname']
          mname = req.POST['mname']
          gender = req.POST['gender']
          dob = req.POST['dob']
          contactno = req.POST['contactno']
          emailaddress = req.POST['emailaddress']
          tclass = req.POST['tclass']
          address = req.POST['address']
          salary = req.POST['salary']
          qualification = req.POST['qualification']
          created_date = timezone.now()
          tl = Teacher(name=name,pic=pic,fname=fname,mname=mname,gender=gender,dob=dob,contactno=contactno,emailaddress=emailaddress,tclass=tclass,address=address,salary=salary,qualification=qualification,password="12345",created_date=created_date)
          tl.save()
          return redirect('adminapp:viewteacher')
        return render(req,'addteacher.html',{'adminid':adminid,'cl':cl})
    except KeyError:
       return redirect('login')

    
@cache_control(no_store = True,no_cache = True,must_revalidate = True)
def viewteacher(req):
    try:
      if req.session['adminid']!=None:
        adminid = req.session['adminid']
        tl = Teacher.objects.all()
        return render(req,'viewteacher.html',{'adminid':adminid,'tl':tl})
    except KeyError:
       return redirect('login')
     
@cache_control(no_store = True,no_cache = True,must_revalidate = True)
def editteacher(req,id):
    try:
      if req.session['adminid']!=None:
        adminid = req.session['adminid']
        tl = Teacher.objects.get(id=id)
        if req.method == 'POST':
          name = req.POST['name']
          fname = req.POST['fname']
          mname = req.POST['mname']
          gender = req.POST['gender']
          dob = req.POST['dob']
          contactno = req.POST['contactno']
          emailaddress = req.POST['emailaddress']
          tclass = req.POST['tclass']
          address = req.POST['address']
          salary = req.POST['salary']
          qualification = req.POST['qualification']
          created_date = timezone.now()
          Teacher.objects.filter(id=id).update(name=name,fname=fname,mname=mname,gender=gender,dob=dob,contactno=contactno,emailaddress=emailaddress,tclass=tclass,address=address,salary=salary,qualification=qualification,password="12345",created_date=created_date)
          return redirect('adminapp:viewteacher')
        return render(req,'editteacher.html',{'adminid':adminid,'tl':tl})
    except KeyError:
       return redirect('login')

def delteacher(req,id):
    try:
      if req.session['adminid']!=None:
         Teacher.objects.get(id=id).delete()
         return redirect('adminapp:viewteacher')
    except KeyError:
       return redirect('login')
    
@cache_control(no_store = True,no_cache = True,must_revalidate = True)    
def addnoti(req):
    try:
      if req.session['adminid']!=None:
        adminid = req.session['adminid']
        if req.method == "POST":
           text = req.POST['text']
           doc = req.POST['doc']
           created_date=datetime.date.today()
           noti = Notification(text=text,doc=doc,created_date=created_date)
           noti.save()
           return redirect('adminapp:viewnoti')
        return render(req,'addnoti.html',{'adminid':adminid})
    except KeyError:
       return redirect('login')
    
@cache_control(no_store = True,no_cache = True,must_revalidate = True)    
def viewnoti(req):
    try:
      if req.session['adminid']!=None:
        adminid = req.session['adminid']
        nt = Notification.objects.all()
        return render(req,'viewnoti.html',{'adminid':adminid,'nt':nt})
    except KeyError:
       return redirect('login')
