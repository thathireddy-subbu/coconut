from django.db import models

class student(models.Model):
    name = models.CharField(max_length=40)
    age = models.IntegerField()
    marks = models.IntegerField()
    college_name = models.CharField(max_length=50)
    city = models.CharField(max_length=40)
    def __str__(self):
        return self.name
