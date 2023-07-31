from django.db import models
from django.contrib.auth.models import User
from .STATE_LIST import STATE_LIST

class Personnel(models.Model):
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE
    )

    username = models.CharField(
        max_length = 32,
        unique = True
    )

    is_employee = models.BooleanField(
        default = False
    )

    def __str__(self):
        return self.username

class Customer(models.Model):
    first_name = models.CharField(
        max_length = 32
    )

    last_name = models.CharField(
        max_length = 32
    )
    
    address = models.CharField(
        max_length = 128
    )
    
    city = models.CharField(
        max_length = 64
    )
    
    state = models.CharField(
        max_length = 32,
        choices = STATE_LIST
    )

    zip_code = models.IntegerField(
        default = 11217
    )
    
    phone_number = models.CharField(
        max_length = 14
    )
    
    email = models.EmailField(
        max_length = 52,
        unique = True
    )

    def __str__(self):
        return f'{self.firstName} {self.lastName}'

class Order(models.Model):
    customer = models.ForeignKey(Customer,
        on_delete = models.CASCADE,
        related_name = 'orders'
    )
    
    order_notes = models.TextField()

    date_ordered = models.DateTimeField("date ordered",
        auto_now = True
    )
    
    def __str__(self):
        return f'{self.customer} {self.id}'
    
class Item(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete = models.CASCADE
    )

    item_description = models.CharField(
        max_length = 255
    )

    item_notes = models.TextField()