import email
from email.policy import default
from django.db import models
from .product import Product
from .customer import Customer
import datetime


class Order(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=50,default="",blank=True)
    phone = models.CharField(max_length=50,default="1234567890",blank=True)
    price = models.IntegerField()
    date = models.DateField(default = datetime.datetime.today)
    status = models.BooleanField(default=False)
    order_id = models.IntegerField(default=0)
    #related to razor pay
    razorpay_order_id = models.CharField(max_length=500,null=True,blank=True)
    razorpay_payment_id = models.CharField(max_length=500,null=True,blank=True)
    razorpay_signature = models.CharField(max_length=500,null=True,blank=True)



    def place_order(self):
        self.save()
    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer = customer_id).order_by("-date")

    @staticmethod
    def get_all_orders():
        return Order.objects.all()
    
    @staticmethod
    def get_order_by_order_id(order_id):
        return Order.objects.filter(order_id = order_id)

