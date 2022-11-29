from django.contrib import admin

from .models import *

admin.site.register(Restaurant)
admin.site.register(Worker)
admin.site.register(Dish)
admin.site.register(Customer)
admin.site.register(Order)
