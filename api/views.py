from django.shortcuts import render
from .models import Employee
from rest_framework import generics
from .serializers import EmployeeSerializer

class EmployeeCreate(generics.CreateAPIView): #new employee creation
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
class EmployeeList(generics.ListAPIView): #employee view
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
class EmployeeDetail(generics.RetrieveAPIView): #returns a single employee
    queryset = Employee.objects.all()
    serializer_class= EmployeeSerializer
    
class EmployeeUpdate(generics.RetrieveUpdateAPIView): # update an employee
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
class EmployeeDelete(generics.RetrieveDestroyAPIView): # delete an employee record
    queryset = Employee.objects.all()
    serializer_class= EmployeeSerializer
    