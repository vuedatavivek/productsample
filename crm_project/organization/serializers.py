from rest_framework import serializers
from .models import Hardware, Software, Employees

class HardwareSerializers(serializers.ModelSerializer):
    class Meta:
        model = Hardware
        fields = ['pk', 'name', 'description', 'created']

class SoftwareSerializers(serializers.ModelSerializer):
    class Meta:
        model = Software
        fields = ['pk', 'name', 'description', 'created']

class EmployeesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ['pk', 'empno', 'name', 'dob', 'doj', 'dept', 'created']
