from . import api
from django.urls import path

urlpatterns = [
    path('products', api.api_products_list, name='products-list'),
    path('products/<int:product_id>/', api.api_product_individual, name='products-individual'),
    path('products/details', api.api_add_products_details, name='add-product-details'),
    path('products/<int:product_id>/details', api.api_products_details, name='product-details'),
    path('products/<int:product_id>/purchase', api.api_products_purchase, name='product-purchase'),
    #path('products/<int:product_id>/purchase', api.api_products_purchase_by_product_id, name='product-purchase-product-id'),
    path('products/order/confirmation', api.api_products_order_confirmation, name='product-order-confirmation'),

    #JUST FRO DEMO
    path('data', api.api_faker_product, name='faker-product'),
]
