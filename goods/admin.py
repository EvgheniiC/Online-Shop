from django.contrib import admin

from goods.models import Categories

from goods.models import Products
from unicodedata import category


# admin.site.register(Categories)
# admin.site.register(Products)

# как будут выглядеть в админ панели дынные
@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}  # Autocomplete slug
    list_display = ['name']


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'quantity', 'price', 'discount']
    list_editable = ['discount']  # что можно изменять в админ панели в ручную
    search_fields = ['name', 'discount']  # поиск в админ панели
    list_filter = ['discount', 'quantity', 'category']
    fields = ['name', 'category', 'slug', 'description', 'image', ('price', 'discount'),
              'quantity']  # ('price', 'discount') будут в одной лии в админ панели
