from django.db import models

class Course(models.Model):
    idno = models.IntegerField(default=2,primary_key=True)
    name = models.CharField(max_length=50)
    duration = models.IntegerField(default=3)
    fee = models.IntegerField(default=5)

class Faculty(models.Model):
    idno = models.IntegerField(default=2,primary_key=True)
    name = models.CharField(max_length=50)
    contact = models.IntegerField(default=10)
    exp = models.DecimalField(max_digits=4,decimal_places=1)
    course = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

class NewClass(models.Model):
    cid = models.IntegerField(default=10,primary_key=True)
    name = models.CharField(max_length=50)
    time = models.TimeField()
    date = models.DateField()
    faculty_name = models.CharField(max_length=50)