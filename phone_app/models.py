from django.db import models

# Create your models here.

class details(models.Model):
    id=models.AutoField
    name=models.CharField(max_length=100)
    date=models.DateField()


class mobile(models.Model):
    id=models.AutoField
    brand=models.CharField(max_length=100,null=True)
    name=models.CharField(max_length=100,null=True)
    price=models.IntegerField(null=True)
    network=models.CharField(max_length=50,null=True)
    display=models.CharField(max_length=300,null=True)
    ram=models.CharField(max_length=100,null=True)
    os=models.CharField(max_length=50,null=True)
    description=models.TextField(null=True)
    img=models.CharField(max_length=200)