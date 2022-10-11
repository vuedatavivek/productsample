from django.db import models

# Create your models here.
class Hardware:
    name = models.CharField("Name", max_length=240)
    description = models.CharField("Description", max_length=500)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class Software:
    name = models.CharField("Name", max_length=240)
    description = models.CharField("Description", max_length=500)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class Employees:
    empno = models.CharField("EmpNo", max_length=10)
    name = models.CharField("Name", max_length=240)
    dob = models.DateField()
    doj = models.DateField()
    dept = models.CharField("Dept", max_length=20)    
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
