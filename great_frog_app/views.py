from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.contrib import auth
from rest_framework.response import Response
from rest_framework import permissions
# from knox.models import AuthToken

from .serializers import UserSerializer, CustomerSerializer, OrderSerializer
from .models import Customer, Order, Personnel, Item

