from django.db import models

class StudentModel(models.Model):
    Name = models.CharField(max_length=100)
    Age = models.IntegerField()
    Subject = models.CharField(max_length=100)
    Marks = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return f"{self.Name}"
    
class Teacher(models.Model):
    Name = models.CharField(max_length=100)
    Age = models.IntegerField()
    Subject = models.CharField(max_length=100)
    Expertice= models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return f"{self.Name}"
    
# New Comment Has been Added
