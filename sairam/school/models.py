from django.db import models
class programs(models.Model):
    coursename = models.CharField(max_length=200)
    age=models.CharField(max_length=200)
    def __str__(self):
        return self.coursename
class details(models.Model):
    course = models.ForeignKey(programs,on_delete=models.CASCADE)
    co=models.CharField(max_length=500)
    ag=models.CharField(max_length=500)
    def __str__(self):
        return self.co



# Create your models here.
