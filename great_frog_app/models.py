from django.db import models
from django.contrib.postgres.fields import ArrayField


class Customer(models.Model):
    firstName = models.CharField(
        # required = True,
        max_length = 30)
    lastName = models.CharField(
        # required = True,
        max_length = 30)
    address = models.CharField(
        # required = False,
        max_length = 128)
    phoneNumber = models.CharField(
        # required = True,
        max_length = 14)
    email = models.EmailField(
        max_length = 52,
        unique = True
    )

    def __str__(self):
        return f'{self.firstName}'

class Order(models.Model):
    firstName = models.OneToOneField(
        Customer,
        on_delete=models.CASCADE,
        related_name='firstNames')
    lastName = models.OneToOneField(
        Customer,
        on_delete=models.CASCADE,
        related_name='lastNames')
    email = models.OneToOneField(
        Customer,
        on_delete=models.CASCADE,
        related_name='emails')
    item = ArrayField(
            models.CharField(
                # required = True,
                max_length = 255
                ))
    dateOrdered = models.DateTimeField(
        auto_now = True)
    
    def __str__(self):
        return f'{self.id}'
    