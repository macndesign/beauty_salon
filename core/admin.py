from django.contrib import admin
from .models import Customer, Staff, Product, Service, Expense


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    pass


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'staff', 'customer', 'product')
    fields = ('staff', 'customer', 'product')


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    pass
