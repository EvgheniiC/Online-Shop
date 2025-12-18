from django import template

from carts.utils import get_user_carts

register = template.Library()

# ПОльзовательский шаблонный тэг,все корзины какого-то ползьзователя, будет испоьзоваться в included_cart
@register.simple_tag()
def user_carts(request):
    return get_user_carts(request)