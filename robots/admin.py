from django.contrib import admin
from .models import Robot, Order, Customer

# Register your models here.


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'email']
    list_display_links = ['email']
    list_per_page = 5
    ordering = ['id']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'robot_serial', 'model', 'version']
    list_display_links = ['id']
    list_per_page = 5
    ordering = ['id']


@admin.register(Robot)
class RobotAdmin(admin.ModelAdmin):
    list_display = ['id', 'serial', 'model', 'version', 'created', 'orders', 'stock']
    list_display_links = ['serial', 'model']
    list_per_page = 15
    ordering = ['id']