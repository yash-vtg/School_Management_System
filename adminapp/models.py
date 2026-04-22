from django.db import models

# Create your models here.


class Classes(models.Model):
    cid = models.IntegerField(primary_key=True,auto_created=True)
    class_name = models.CharField(max_length=30)
    seats = models.IntegerField()
    roomno = models.CharField(max_length=50)
    created_date = models.DateTimeField()

class Subject(models.Model):
    sid = models.IntegerField(primary_key=True,auto_created=True)
    subject_name = models.CharField(max_length=30)
    sclass = models.CharField(max_length=50)
    book = models.CharField(max_length=50)
    steacher = models.CharField(max_length=50)
    created_date = models.DateTimeField()

class Teacher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    fname = models.CharField(max_length=50)
    mname = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    dob = models.CharField(max_length=15)
    contactno = models.CharField(max_length=20)
    emailaddress = models.EmailField(max_length=50, unique=True)
    tclass = models.CharField(max_length=30)
    address = models.TextField()
    salary = models.CharField(max_length=10)
    qualification = models.CharField(max_length=50)
    pic = models.ImageField(upload_to='')
    password = models.CharField(max_length=30)
    created_date = models.DateTimeField()

class Student(models.Model):
    rollno = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    fname = models.CharField(max_length=50)
    mname = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    dob = models.CharField(max_length=15)
    contactno = models.CharField(max_length=20)
    emailaddress = models.EmailField(max_length=50, unique=True)
    address = models.TextField()
    sclass = models.CharField(max_length=30)
    feespaid = models.CharField(max_length=10)
    duefees = models.CharField(max_length=10)
    password = models.CharField(max_length=30)
    pic = models.ImageField(upload_to='')
    created_date = models.DateTimeField()

class Attendence(models.Model):
    sid = models.CharField(max_length=10)
    rollno = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    sclass = models.CharField(max_length=30)
    tclass = models.CharField(max_length=30)
    status = models.CharField(max_length=1)
    created_date = models.DateField()

class Notification(models.Model):
    text = models.TextField()
    doc = models.FileField()
    created_date = models.DateField()
