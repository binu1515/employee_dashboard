from .models import CHECK, Employees, visitor
from django import forms


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employees
        fields = "__all__"

CHECK= [
    ('checked', 'Checkin'),
    ('inside', 'Inside'),
    ('out', 'Checkout'),
    ]

class visitorForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    contact = forms.BigIntegerField()
    location = forms.CharField(max_length=100)
    employee = forms.CharField(max_length=100)
    visitorstatus = forms.CharField(max_length=100,choices=CHECK)



  




class visitorForm(forms.ModelForm):
    class Meta:
        model = visitor
        fields = '__all__'