from django.contrib import admin

from carts.models import Cart


# чтобы корзина(пользователей) показывалась в админ панеле для АДМИНОВ
class CartTabAdmin(admin.TabularInline):
    model = Cart  # модель
    extra = 1  # СВОбОДНЫЕ ПОЛЯ ДЛЯ доюавления пользователем новых заказов
    fields = ('product', 'quantity', 'created_timestamp')  # поля в онлайн режиме
    readonly_fields = ('created_timestamp',)  # нельзя изменять
    search_fields = ('product', 'quantity', 'created_timestamp')


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'quantity', 'created_timestamp']
    list_filter = ['user', 'product__name', 'created_timestamp']  # product__name это foreign key

    def user_display(self, obj):
        if obj.user:
            return str(obj.user.username)
        return "Anonymous"

    def product_display(self, obj):
        return str(obj.product.name)
