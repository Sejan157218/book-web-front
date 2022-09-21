from django.db import models
import datetime
from django.utils.translation import gettext as _
from django.contrib.postgres.fields import ArrayField

# Create your models here.


class Category(models.Model):
    title=models.CharField(max_length=200)
    date=models.DateField(auto_now_add=True)
    def __str__(self) :
        return self.title



class Author(models.Model):
    name=models.CharField(max_length=300)
    image =models.ImageField(upload_to="authors/")
    date=models.DateField(auto_now_add=True)
    def __str__(self) :
        return self.name


class Publisher(models.Model):
    name=models.CharField(max_length=300)
    date=models.DateField(auto_now_add=True)
    def __str__(self) :
        return self.name




YEAR_CHOICES = [(r,r) for r in range(1984, datetime.date.today().year+1)]
class Book(models.Model):
    category=models.ForeignKey(Category,on_delete=models.SET_NULL,blank=True,null=True)
    publisher=models.ForeignKey(Publisher,on_delete=models.SET_NULL,blank=True,null=True)
    author=models.ForeignKey(Author,on_delete=models.SET_NULL,blank=True,null=True)
    title=models.CharField(max_length=200)
    date=models.DateField(auto_now_add=True)
    market_price=models.IntegerField()  
    selling_Price=models.IntegerField(null=True, blank=True)
    discount_percent  = models.FloatField(null=True, blank=True)
    description=models.TextField()
    edition_number=models.CharField(max_length=10,default=None)
    edition_year = models.IntegerField(_('year'), choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    stock=models.IntegerField(default=None)
    image =models.ImageField(upload_to="book/")



    @property
    def selling_Price(self):
        if self.discount_percent is not None and self.discount_percent  > 0:
            discounted_price = self.market_price - self.market_price * self.discount_percent  / 100
            return round(discounted_price, 2)
        else:
            return self.market_price

    def __str__(self):
        return self.title




ORDER_STATUS={
    ("Order Received","Order Received"),
    ("Order Processing","Order Processing"),
    ("On the way","On the way"),
    ("Order Completed","Order Completed"),
    ("Order Canceled","Order Canceled"),
}



class Order(models.Model):
    user=models.EmailField(default=None,null=True,blank=True)
    book =  ArrayField(models.JSONField(blank=True, null = True))
    totalPrice=models.CharField(max_length=30,blank=True)
    order_status=models.CharField(max_length=100,choices=ORDER_STATUS,default="Order Received")
    date=models.DateField(auto_now_add=True,null=True)
    def __str__(self):
        return self.user
