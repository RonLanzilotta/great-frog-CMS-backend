from django.db import models

class Customer(models.Model):
    firstName = models.CharField(
        max_length = 30)
    lastName = models.CharField(
        max_length = 30)
    address = models.CharField(
        max_length = 128)
    phoneNumber = models.CharField(
        max_length = 14)
    email = models.EmailField(
        max_length = 52,
        unique = True
    )

    def __str__(self):
        return f'{self.firstName} {self.lastName}'
        # return f'{self.id}'


class Order(models.Model):
    customer = models.ForeignKey(Customer,
        on_delete = models.CASCADE,
        related_name = 'orders'
        )
    item = models.CharField(
        max_length = 255
        )
    notes = models.CharField(
        max_length = 255
        )
    dateOrdered = models.DateTimeField("date ordered",
        auto_now = True)
    
    def __str__(self):
        return f'{self.customer} {self.id}'
    