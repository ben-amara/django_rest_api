from . import api
from django.urls import path

urlpatterns = [
    path('order/confirmation', api.api_order_confirmation, name='order-confirmation'),
    path('order/create', api.api_order_create, name='order-create'),
    path('product/<int:product_id>/description', api.api_product_description, name='product-description'),
    path('product/<int:product_id>/list', api.api_product_list, name='product-list'),
]
