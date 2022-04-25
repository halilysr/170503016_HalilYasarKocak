from pyexpat import model
from unicodedata import name
from django.db import models

# Create your models here.

class Training(models.Model):
    trainer = models.ForeignKey("auth.User", on_delete= models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(default=" ")

    def __str__(self):
        return self.name
    