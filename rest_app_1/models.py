from django.db import models

# Create your models here.

class Post(models.Model):
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=100)


class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField()

    
    def __str__(self):
        return self.name