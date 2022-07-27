from pyexpat import model
from django.db import models

# Create your models here.

class Student(models.Model):
    fname=models.CharField(max_length=255)
    lname=models.CharField(max_length=255)
    
    def __str__(self):
        
        return '{} \t {}'.format(self.fname, self.lname)
    
class Course(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    course_name=models.CharField(max_length=200)  
    
    def __str__(self):
        return self.course_name
    
class Cars(models.Model): 
    name=models.CharField(max_length=200)
    brand=models.CharField(max_length=200) 
    price=models.FloatField()
    
    
    def __str__(self):
        return self.name  
    
