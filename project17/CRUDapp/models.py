from django.db import models

# Create your models here.
class Student(models.Model):
    student_name = models.CharField(max_length=50)
    student_mail = models.EmailField()
    student_phoneno = models.IntegerField()
    student_address = models.CharField(max_length=50)

