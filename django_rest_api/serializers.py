from rest_framework import serializers
from .models import ( Products, ProductType, ProductCategory, Customer, CustomerPhone, ShippingAddress, BillingAddress,
                    PurchaseProducts, OrderConfirmation )

class ProductsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Products
        fields = ('code', 'name', 'cost', 'description', 'inventory_on_hand')
