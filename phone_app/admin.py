from django.contrib import admin
from .models import profile,mobile,card,cart,orders
# Register your models here.

admin.site.register(profile)
admin.site.register(mobile)
admin.site.register(card)
admin.site.register(cart)
admin.site.register(orders)