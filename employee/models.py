from django.db import models

# Create your models here.


class Employee(models.Model):
    first_name = models.CharField(max_length=100,default="")
    last_name = models.CharField(max_length=100,default="")
    bonus = models.IntegerField(default=0)
    salary = models.IntegerField(default=0)
    phone = models.IntegerField(default=0)
    role_name= models.CharField(max_length=200,default="")
    dept_name = models.CharField(max_length=200,default="")
    location = models.CharField(max_length=500,default="")


    def __str__(self):
        return self.first_name
    

