from django.db import models

# Create your models here.

class Sender(models.Model):
    to = models.CharField(max_length=30,default=5)
    sub = models.CharField(max_length=50) 
    msg = models.TextField() 

    def __str__(self):
        return "User-"+ self.to
    
