from django.contrib import admin
from .models import Customer, Order

admin.site.register(Order)
admin.site.register(Customer)