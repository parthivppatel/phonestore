from django.db import models
from django.contrib.auth.models import User
# Create your models here.
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

class profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    phone=models.TextField(max_length=10,null=False)
    pincode=models.IntegerField(null=True)
    country=models.TextField(max_length=10,null=True)
    flat=models.TextField(max_length=100,null=True)
    area=models.TextField(max_length=150,null=True)
    landmark=models.TextField(max_length=100,null=True)
    state=models.TextField(max_length=50,null=True)
    city=models.TextField(max_length=50,null=True)

class cart(models.Model):
    user= models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    product=models.ForeignKey(mobile,to_field='id',on_delete=models.CASCADE,null=True)
    is_order=models.BooleanField(null=True)
    quantity=models.IntegerField(null=True)
    date=models.DateField(null=True)
    subtotal=models.IntegerField(null=True)

class orders(models.Model):
    user= models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    product=models.ForeignKey(mobile,to_field='id',on_delete=models.CASCADE,null=True)
    date=models.DateField()
    status=models.TextField()
    quantity=models.IntegerField()
    total=models.IntegerField()
    cart=models.ForeignKey(cart,null=True,on_delete=models.CASCADE)

class card(models.Model):
    name=models.TextField()
    number=models.TextField()
    expiry=models.TextField()
    cvv=models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)