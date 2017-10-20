from django.db import models
from account.models import Owner, Customer

# Create your models here.
class Shop_particulars(models.Model):
    nric = models.ForeignKey(Owner, on_delete=models.CASCADE, verbose_name="Stall Owner IC")
    stall_id = models.CharField(max_length=6, primary_key=True)
    stall_name = models.CharField(max_length=100)
    block_no = models.CharField(max_length=10, null=True)
    street_no = models.CharField(max_length=50)
    stall_no = models.CharField(max_length=10)
    postal_cd = models.CharField(max_length=6)
    country = models.CharField(max_length=50)
    start_operation_time = models.CharField(max_length=5) # hh:mm
    end_operation_time = models.CharField(max_length=5)
    operation_days = models.CharField(max_length=50)
    remarks = models.CharField(max_length=500, null=True)

class Menu(models.Model):
    stall_id = models.ForeignKey(Shop_particulars,on_delete=models.CASCADE, verbose_name="Stall ID")
    item_id = models.CharField(max_length=4)
    item_name = models.CharField(max_length=100)
    item_price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=500)
    recommended_consume_time = models.CharField(max_length=100)

class OrderStatus(models.Model):
    ord_status_cd = models.CharField(max_length=4, primary_key=True)
    order_status = models.CharField(max_length=40)

class Order(models.Model):
    order_no = models.CharField(max_length=8, primary_key=True)
    order_date = models.DateField()
    order_time = models.TimeField()
    email = models.ForeignKey(Customer)
    order_qty = models.IntegerField()
    stall_id = models.ForeignKey(Shop_particulars,on_delete=models.CASCADE, verbose_name="Stall ID")
    ord_status_cd = models.ForeignKey(OrderStatus, on_delete=models.CASCADE, verbose_name="Order Status ID")

class Feedback(models.Model):
    feedback_id = models.CharField(max_length=10, primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    stall_id = models.ForeignKey(Shop_particulars, on_delete=models.CASCADE)
    ratings = models.IntegerField()
    comments = models.CharField(max_length=500)

class CustomerRatings(models.Model):
    ratings_id = models.CharField(max_length=10, primary_key=True)
    ratings = models.IntegerField()
    comments = models.CharField(max_length=500)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    stall_id = models.ForeignKey(Shop_particulars, on_delete=models.CASCADE)