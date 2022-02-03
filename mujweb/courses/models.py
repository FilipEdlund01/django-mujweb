from tracemalloc import start
from turtle import title
from django.db import models

# Create your models here.

class Teacher (models.Model):
    name = models.CharField(max_length=225)

    def __str__(self):
        return f"Ucitel jmenem {self.name} ma ID {self.pk} "

class Course(models.Model):
    title = models.CharField(max_length=225)
    start = models.DateField()


