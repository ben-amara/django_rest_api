from rest_framework import serializers
from .models import ( Products, OrderConfirmation, ProductDetails, OrderCreate )

class ProductsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Products
        fields = ('code', 'name', 'cost', 'description', 'inventory_on_hand')


class ProductDetailsSerializer(serializers.ModelSerializer):
    product = ProductsSerializer()
    class Meta:
        model = ProductDetails
        fields = ('product', 'product_type', 'category')

class OrderConfirmationSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderConfirmation
        fields = ('order_confirmation', 'customer_phone', 'purchase_products', 'order_total')

class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderCreate
        fields = ('customer_name', 'customer_email', 'customer_phone', 'shipping_address', 'billing_address', 'purchase_products')
