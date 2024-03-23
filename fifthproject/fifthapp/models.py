from django.db import models

# Create your models here.
class student(models.Model):
    studentname=models.IntegerField()
    studentage=models.CharField(max_length=20)
