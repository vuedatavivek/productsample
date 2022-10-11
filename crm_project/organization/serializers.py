from rest_framework import serializers
from .models import Hardware, Software, Employees

class HardwareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hardware
        fields = ['pk', 'name', 'description', 'created']

class SoftwareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Software
        fields = ['pk', 'name', 'description', 'created']

class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ['pk', 'empno', 'name', 'dob', 'doj', 'dept', 'created']
