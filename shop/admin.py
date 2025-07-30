from django.contrib import admin
from .models import products, cartitem, orders

admin.site.register(products)
admin.site.register(cartitem)
admin.site.register(orders)

# Register your models here.
