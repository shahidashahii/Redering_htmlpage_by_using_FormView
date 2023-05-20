from django.db import models

# Create your models here.
class School(models.Model):
    Sname=models.CharField(max_length=100,primary_key=True)
    Sage=models.IntegerField()
    Sadress=models.TextField(max_length=100)
    Smno=models.IntegerField()