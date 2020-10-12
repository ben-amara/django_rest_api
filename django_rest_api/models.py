# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Products(models.Model):
    code = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    name = models.CharField(max_length=255, blank=True, null=True)
    cost = models.IntegerField(default=0)
    description = models.TextField(blank=True, null=True)
    inventory_on_hand = models.IntegerField(default=0)
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)

    class Meta:
        db_table = 'products'

class ProductType(models.Model):
    product_type_id = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    type_name = models.CharField(max_length=255, blank=True, null=True)
    type_product = models.CharField(max_length=255, blank=True, null=True)
    product = models.ForeignKey(Products, models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)

    class Meta:
        db_table = 'product_type'

class ProductCategory(models.Model):
    product_category_id = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    name = models.CharField(max_length=255, blank=True, null=True)
    type_category = models.CharField(max_length=255, blank=True, null=True)
    product = models.ForeignKey(Products, models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)

    class Meta:
        db_table = 'product_category'

class Customer(models.Model):
    customer_id = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    customer_name = models.CharField(max_length=255, blank=True, null=True)
    customer_mail = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)

    class Meta:
        db_table = 'customer'

class CustomerPhone(models.Model):
    customer_phone_id = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    customer  = models.ForeignKey(Customer, models.DO_NOTHING, blank=True, null=True)
    contact = models.BooleanField(default=True, blank=True, null=True)
    type_number = models.CharField(max_length=255, blank=True, null=True)
    number = models.IntegerField(default=0)
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)

    class Meta:
        db_table = 'customer_phone'

class ShippingAddress(models.Model):
    shipping_address_id = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    customer  = models.ForeignKey(Customer, models.DO_NOTHING, blank=True, null=True)
    street = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    zipcode = models.IntegerField(default=0)
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)

    class Meta:
        db_table = 'shipping_address'


class BillingAddress(models.Model):
    shipping_address_id = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    customer  = models.ForeignKey(Customer, models.DO_NOTHING, blank=True, null=True)
    street = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    zipcode = models.IntegerField(default=0)
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)

    class Meta:
        db_table = 'billing_address'


class PurchaseProducts(models.Model):
    purchase_products_id = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    code  = models.ForeignKey(Products, models.DO_NOTHING, blank=True, null=True)
    quantity = models.IntegerField(default=0)
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)

    class Meta:
        db_table = 'purchase_products'

class OrderConfirmation(models.Model):
    order_confirmation_id = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    order_confirmation = models.CharField(max_length=255, blank=True, null=True)
    customer_phone  = models.ForeignKey(CustomerPhone, models.DO_NOTHING, blank=True, null=True)
    purchase_products  = models.ForeignKey(PurchaseProducts, models.DO_NOTHING, blank=True, null=True)
    order_total = models.IntegerField(default=0)
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)

    class Meta:
        db_table = 'order_confirmation'

















