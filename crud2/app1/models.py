from django.db import models

# Create your models here.

class Employee(models.Model):
    idno = models.IntegerField(unique=True)
    name = models.CharField(max_length=20)
    salary = models.FloatField()
