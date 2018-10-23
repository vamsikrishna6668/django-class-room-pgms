from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=50)
    cno = models.IntegerField(default=10,primary_key=True)
    desingation = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=10,decimal_places=2)

