from django.contrib import admin
from .models import Product,Order,OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem

class OrderAdmin(admin.ModelAdmin):
    list_display = ('__str__', )
    inlines = [OrderItemInline]
    search_fields = ['contact']


admin.site.register(Product)
admin.site.register(Order, OrderAdmin)
