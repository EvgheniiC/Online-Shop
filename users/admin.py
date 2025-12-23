from django.contrib import admin
from users.models import User

from carts.admin import CartTabAdmin


# admin.site.register(User) # если ничего не надо менять

# если хочешь вижеть свои настройки и параметры
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'email']
    search_fields = ['username', 'first_name', 'last_name', 'email']

    inlines = [CartTabAdmin] # делаем корзину пользователя для админов видимой
#
#
# @admin.register(Products)
# class ProductsAdmin(admin.ModelAdmin):
#     prepopulated_fields = {'slug': ('name',)}
