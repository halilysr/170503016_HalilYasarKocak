from pyexpat import model
from unicodedata import name
from django.db import models
from matplotlib import image

# Create your models here.


class Training(models.Model):

    trainer = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(default=" ")
    image = models.FileField(blank= True, null= True, verbose_name="Add an image")

    def __str__(self):
        return self.name
    