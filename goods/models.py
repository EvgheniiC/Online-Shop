from decimal import Decimal

from django.db import models


# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'category'
        verbose_name = 'Категорию'  # visual table name in admin panel
        verbose_name_plural = 'Категории'  # visual table name in admin panel plural


class Products(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='описание')
    image = models.ImageField(upload_to='goods_image', null=True, blank=True, verbose_name='Изоражение')
    price = models.DecimalField(default=0.0, max_digits=7, decimal_places=2, verbose_name='Цена')
    discount = models.DecimalField(default=0.0, max_digits=7, decimal_places=2, verbose_name='Скидка в %')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE, verbose_name='Категория')

    # To see correct Product name in admin panel
    def __str__(self):
        return f'{self.name} Количество - {self.quantity} '

    class Meta:
        db_table = 'product'
        verbose_name = 'Продукт'  # visual table name in admin panel
        verbose_name_plural = 'Продукты'  # visual table name in admin panel plural
        ordering = ("id",) # for pagination

    # 7 -> 00007
    def display_id(self) -> str:
        return f"{self.id:05}"

    def sell_price(self) -> Decimal:
        if self.discount:
            return round(self.price - self.price * self.discount / 100, 2)
        return self.price
