from django.contrib import admin
from .models import Customer, Order


# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number')
    search_fields = ('first_name', 'last_name', 'email')

# Register the Order model with admin
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'order_date', 'total_amount', 
'is_paid')
    list_filter = ('order_date', 'is_paid')
    search_fields = ('customer__first_name', 'customer__last_name', 'id') 

