from django.db import models

from goods.models import Products
from users.models import User


# for all carts from one user
class CartQuerySet(models.QuerySet):
    def total_price(self):
        return sum(cart.products_price() for cart in self)

    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0


class Cart(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Polzovatel")
    product = models.ForeignKey(to=Products, on_delete=models.CASCADE, verbose_name="Tovar")
    quantity = models.PositiveIntegerField(default=0, verbose_name="Kolichestvo")
    session_key = models.CharField(max_length=32, null=True, blank=True, verbose_name="Session Key")
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Date to add")

    class Meta:
        verbose_name = "Cart"
        verbose_name_plural = "Carts"

    # for all carts from one user
    objects = CartQuerySet.as_manager()

    def products_price(self):
        return round(self.product.sell_price() * self.quantity, 2)

    def __str__(self):
        return f'Korzina {self.user.username} | Tovar {self.product.name} | Kolichestvo {self.quantity}'
