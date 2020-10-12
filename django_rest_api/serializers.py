from rest_framework import serializers
from .models import ( Products, OrderConfirmation, ProductDetails )

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
