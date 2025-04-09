from django.contrib import admin
from .models import Category, Product, Client, Order

# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')
    search_fields = ('title',)

    def has_change_permission(self, request, obj=None):
        return False  # Categoriyalar odatda ozgartirilmaydi


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'price', 'available', 'created_at')
    list_filter = ('available', 'category')
    search_fields = ('name', 'description')
    readonly_fields = ('created_at',)

    def has_change_permission(self, request, obj=None):
        return Product # Srogini ozgartirmasligi uchun


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone_number', 'email', 'address', 'date_of_ordering')
    search_fields = ('name', 'phone_number', 'email')
    readonly_fields = ('date_of_ordering',)

    def has_change_permission(self, request, obj=None):
        return True


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'product', 'quantity', 'status', 'delivery')
    list_filter = ('status', 'delivery')
    search_fields = ('client__name', 'product__name')

    def has_change_permission(self, request, obj=None):
        return True
