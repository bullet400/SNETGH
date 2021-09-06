from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    MY_TITLE =(
        ('mr','Mr'),
        ('mrs','Mrs'),
        ('dr','Dr'),
    )
    title =models.CharField(max_length=20, choices = MY_TITLE)
    first_name = models.CharField(max_length =30, null=True)
    last_name = models.CharField(max_length =50, null= True)
    user =models.OneToOneField(User, null= True, on_delete=models.CASCADE)
    phone = models.CharField(max_length= 12, null=True)
    email = models.EmailField(max_length=50, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        fullname =self.first_name + " "+ self.last_name
        return fullname.title()

class Tag(models.Model):
    name =models.CharField(max_length=20, null =True)
    date_created =models.DateTimeField(auto_now_add=True, null =True)

    def __str__(self):
        return self.name.upper()

class Product(models.Model):

    CATEGORY =(
        ('indoor','Indoor'),
        ('Kitchen','Kitchen'),
        ('outdoor','OutDoor')
    )
    product_name =models.CharField(max_length=50)
    price       = models.FloatField(max_length=10, null=True)
    quantity    = models.IntegerField()
    category    = models.CharField(max_length=20, null= True, choices=CATEGORY)
    description = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    tag =models.ManyToManyField(Tag)
    def __str__(self):
        return self.product_name.title()
    

class Order(models.Model):
    STATUS =(
        ('Pending','Pending'),
        ('Out for Delivery','Out for Delivery'),
        ('Delivered','Delivered')
        
    )
    customer =models.ForeignKey(Customer, on_delete=models.SET_NULL, null =True)
    product = models.ForeignKey(Product, on_delete= models.SET_NULL, null=True)
    status =models.CharField(max_length=20, choices=STATUS)
    date_created =models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.status

