from django.db import models
class Intro(models.Model):
    first_name = models.CharField(max_length=255,unique=True)
    last_name = models.CharField(max_length=255,unique=True)
    email = models.CharField(max_length=255,unique=True)
    def __str__(self):
        return self.all()

# Create your models here.
