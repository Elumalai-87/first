from django.db import models

# Create your models here.
class studies(models.Model):
    course_name=models.CharField(max_length=90)
    course_id=models.IntegerField()
    course_details=models.CharField(max_length=100)
    course_amount=models.IntegerField()
    course_feedback=models.CharField(max_length=100)
    
