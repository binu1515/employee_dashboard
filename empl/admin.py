from django.contrib import admin

from .models import visitor
from .models import Employees
# Register your models here.
admin.site.register(Employees)
admin.site.register(visitor)