from django import template

from carts.models import Cart

register = template.Library()

# ПОльзовательский шаблонный тэг,все корзины какого-то ползьзователя, будет испоьзоваться в included_cart
@register.simple_tag()
def user_carts(request):
    if request.user.is_authenticated:
        return Cart.objects.filter(user=request.user)