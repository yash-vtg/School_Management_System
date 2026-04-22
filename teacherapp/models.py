from django.db import models
from adminapp.models import *
from django.utils import timezone

# Create your models here.
class StudyMaterial(models.Model):
    fk = models.ForeignKey(Teacher, to_field='emailaddress', on_delete = models.CASCADE, null=True)
    title = models.CharField(max_length=200)
    sm = models.FileField(upload_to='')
    tclass = models.CharField(max_length=30)
    created_date = models.DateField(default=timezone.now)

