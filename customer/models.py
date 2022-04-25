from django.db import models

# Create your models here.
class Customer(models.Model):
    customer = models.ForeignKey("auth.User", on_delete= models.CASCADE)
    name = models.CharField(max_length=100)
    height = models.CharField(max_length= 50)
    weight = models.CharField(max_length= 50)
    attendance = models.CharField(max_length= 50)

    def __str__(self):
        return self.name
    