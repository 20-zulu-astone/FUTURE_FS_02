from django.contrib import admin
from .models import products, cartitem, Order

admin.site.register(products)
admin.site.register(cartitem)
admin.site.register(Order)

# Register your models here.
