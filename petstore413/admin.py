from django.contrib import admin
from petstore413.models import Pet, Product, Cart, CartItem

# Register your models here.
admin.site.register(Pet)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartItem)