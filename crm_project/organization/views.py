from django.shortcuts import render
from .models import Hardware, Software, Employees
from rest_framework import generics
from .serializers import HardwareSerializer, SoftwareSerializer, EmployeesSerializer
from django.db.models.query import Q

# Create your views here.
class CreateHardware(generics.CreateAPIView):
    QuerySet = Hardware.objects.all(),
    serializer_class = HardwareSerializer

class UpdateHardware(generics.RetrieveUpdateAPIView):
    QuerySet = Hardware.objects.all(),
    serializer_class = HardwareSerializer

class DeleteHardware(generics.RetrieveDestroyAPIView):
    QuerySet = Hardware.objects.all(),
    serializer_class = HardwareSerializer

class ListHardware(generics.ListAPIView):
    # queryset = Hardware.objects.all(),
    serializer_class = HardwareSerializer
    def get_queryset(self):
        qs = Hardware.objects.all()
        qs = qs.filter(pk != 1)
        qs =  qs.exclude(name = '')

        #qs = [q for q in qs if q.name != '']
        #qs = qs.filter(Q('name') != '')
        # query = self.request.GET.get('q')

        # if query is not None:
        #     qs = qs.filter().distinct()
        return qs

class DetailHardware(generics.RetrieveAPIView):
    QuerySet = Hardware.objects.all(),
    serializer_class = HardwareSerializer