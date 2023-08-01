from rest_framework import viewsets
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.contrib import auth
from rest_framework.response import Response
from rest_framework import permissions
from knox.models import AuthToken

from .serializers import CustomerSerializer, OrderSerializer, PersonnelSerializer, ItemSerializer
from .models import Customer, Order, Personnel, Item

class PersonnelViewSet(viewsets.ModelViewSet):
    queryset = Personnel.objects.all()
    serializer_class = PersonnelSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class TotalCustomers(APIView):
    permission_classes = [
        permissions.IsAdminUser,
        permissions.IsAuthenticated
    ]
    def get(self, request):
        try:
            results = Customer.objects.all()
            total_customers = CustomerSerializer(
                results, 
                many = True
            )
            return Response(total_customers.data)
        except:
            return Response({"Error": "An error occurred in retrieving the requested information"})
    def post(self, request):
        try:
            personnel = self.request.personnel
            is_admin = personnel.is_staff
            is_auth = personnel.is_authenticated
            if is_admin and is_auth:
                first_name = request.data['first_name']
                last_name = request.data['last_name']
                address = request.data['address']
                city = request.data['city']
                state = request.data['state']
                zip_code = request.data['zip_code']
                phone_number = request.data['phone_number']
                email = request.data['email']
                Customer.objects.create(first_name = first_name, last_name = last_name, address = address, city = city, state = state, zip_code = zip_code, phone_number = phone_number, email = email)
                return Response({'Success': 'Customer successfully created'})
            else:
                return Response({'Error': 'Personnel is not an authenticated administrator'})
        except Exception as e:
            return Response({'Error': 'Invalid body'})

class IndividualCustomerViewSet(APIView):
    permission_classes = [
        permissions.IsAdminUser,
        permissions.IsAuthenticated
    ]
    def get(self, request):
        try:
            customer_results = Customer.objects.get(id = id)
            customer = CustomerSerializer(customer_results)
            order_results = Order.objects.get(customer = customer_results.id)
            orders = OrderSerializer(order_results)
            item_results = Item.objects.get(order = order_results.id)
            item = ItemSerializer(item_results)
            return Response({f'{customer.data}\n{orders.data}\n{item.data}'})
        except:
            return Response({'Error': 'An error occurred retrieving the customer information'})
        
