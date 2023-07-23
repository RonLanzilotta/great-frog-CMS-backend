from rest_framework import serializers
from .models import Customer, Order, Item, Personnel

class PersonnelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personnel
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class CustomerSerializer(serializers.BaseSerializer):
    def to_representation(self, instance):
        return {
            "id": instance.id,
            "first_name": instance.first_name,
            "last_name": instance.last_name,
            "address": instance.address,
            "city": instance.city,
            "state": instance.state,
            "phone_number": instance.phone_number,
            "email": instance.email
        }
    
class OrderSerializer(serializers.BaseSerializer):
    def to_representation(self, instance):
        return {
            "id": instance.id,
            "customer": instance.customer.id,
            "order_notes": instance.order_notes,
            "date_ordered": instance.date_ordered
        }
    
class ItemSerializer(serializers.BaseSerializer):
    def to_representation(self, instance):
        return {
            "id": instance.id,
            "order": instance.order.id,
            "item_description": instance.order_description,
            "item_notes": instance.item_notes
        }