from django.db import models

class Customer(models.Model):
    name=models.CharField(max_length=200,null=True)
    phone=models.CharField(max_length=10,null=True)
    email=models.CharField(max_length=200,null=True)
    datecreated=models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name=models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.name

    
class Product(models.Model):
    CATEGORY=(
        ('Starters','Starters'),
        ('Snacks','Snacks'),
        ('Severages','Beverages'),
        ('Burgers','Burgers'),
        ('Fries','Fries')
    )
    name=models.CharField(max_length=200,null=True)
    price=models.FloatField(null=True)
    category=models.CharField(max_length=200,null=True,choices=CATEGORY)
    description=models.CharField(max_length=200,null=True)
    datecreated=models.DateTimeField(auto_now_add=True,null=True)
    tag=models.ManyToManyField(Tag)
    
    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS=(
        ('pending','Pending'),
        ('out for delivery','Out for Delivery'),
        ('delivered','Delivered')
    )
    customer=models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)
    product=models.ForeignKey(Product,null=True,on_delete=models.SET_NULL)
    datecreated=models.DateTimeField(auto_now_add=True,null=True)
    status=models.CharField(max_length=200,null=True,choices=STATUS)
    