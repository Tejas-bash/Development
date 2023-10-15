from django.db import models

class StudentModel(models.Model):
    Name = models.CharField(max_length=100)
    Age = models.IntegerField()
    Subject = models.CharField(max_length=100)