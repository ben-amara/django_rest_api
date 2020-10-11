from . import api
from django.urls import path

urlpatterns = [
    path('products', api.api_products_list, name='products-list'),
    path('products/<int:product_id>/', api.api_product_individual, name='products-individual'),
    path('products/<int:product_id>/details', api.api_products_details, name='product-details'),
    path('products/<int:product_id>/purchase', api.api_products_purchase, name='product-purchase'),
]
