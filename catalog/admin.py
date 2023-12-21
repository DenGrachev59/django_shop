from django.contrib import admin

from catalog.models import Category, Product
from django.contrib import admin


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)
    search_fields = ('name',)


@admin.register(Product)
class DogAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'category', 'price')
    list_filter = ('category',)
    search_fields = ('name', 'category',)
