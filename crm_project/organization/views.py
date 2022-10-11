from django.shortcuts import render
from .models import Hardware, Software, Employees
from rest_framework import generics
from .serializers import HardwareSerializers, SoftwareSerializers, EmployeesSerializers

# Create your views here.
class CreateHardware(generics.CreateAPIView):
    queryset = Hardware.objects.all(),
    serializer_class = HardwareSerializers

class UpdateHardware(generics.RetrieveUpdateAPIView):
        queryset = Hardware.objects.all(),
        serializer_class = HardwareSerializers

class DeleteHardware(generics.RetrieveDestroyAPIView):
        queryset = Hardware.objects.all(),
        serializer_class = HardwareSerializers

class ListHardware(generics.ListAPIView):
        queryset = Hardware.objects.all(),
        serializer_class = HardwareSerializers

class DetailHardware(generics.RetrieveAPIView):
        queryset = Hardware.objects.all(),
        serializer_class = HardwareSerializers