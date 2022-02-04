from basic.models import Product
from django.contrib import admin

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','description','price')
    list_filter = ('name','price')
    search_fields=('name',)
    ordering = ('name','price')

