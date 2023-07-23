from django.contrib import admin
from .models import Customer, Order, Personnel, Item

admin.site.register(Personnel)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Item)