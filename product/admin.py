from django.contrib import admin

from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    '''catagory management config'''
    list_display = ['name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    '''product management config'''
    list_display = ['name','price', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
