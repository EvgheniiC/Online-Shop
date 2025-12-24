from django.urls import path, URLPattern
from orders import views

app_name = 'orders'

urlpatterns :list[URLPattern] = [
    path('create-order/', views.create_order, name='create_order')
]
