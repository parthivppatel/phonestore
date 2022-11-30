from django.db import models

# Create your models here.

class details(models.Model):
    id=models.AutoField
    name=models.CharField(max_length=100)
    date=models.DateField()
