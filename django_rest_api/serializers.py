from rest_framework import serializers
from .models import ( Products, ProductType, ProductCategory, Customer, CustomerPhone, ShippingAddress, BillingAddress,
                    PurchaseProducts, OrderConfirmation, ProductDetails )

class ProductsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Products
        fields = ('code', 'name', 'cost', 'description', 'inventory_on_hand')

class ProductTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductType
        fields = ('type_name', 'type_product')

class ProductCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductCategory
        fields = ('name', 'type_category')

class CustomerPhoneSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductCategory
        fields = ('contact', 'type_number', 'number')

class PurchaseProductsSerializer(serializers.ModelSerializer):

    class Meta:
        model = PurchaseProducts
        fields = ('code', 'quantity')

class ProductDetailsSerializer(serializers.ModelSerializer):
    product = ProductsSerializer()
    product_type = ProductTypeSerializer()
    category = ProductCategorySerializer()
    class Meta:
        model = ProductDetails
        fields = ('product', 'product_type', 'category')

class OrderConfirmationSerializer(serializers.ModelSerializer):
    product = ProductsSerializer()
    customer_phone = CustomerPhoneSerializer()
    purchase_products = PurchaseProductsSerializer()
    class Meta:
        model = OrderConfirmation
        fields = ('order_confirmation', 'customer_phone', 'purchase_products', 'order_total')
