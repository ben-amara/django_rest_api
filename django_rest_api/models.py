# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.postgres.fields import JSONField



class Products(models.Model):
    code = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    name = models.CharField(max_length=255, blank=True, null=True)
    cost = models.IntegerField(default=0)
    description = models.TextField(blank=True, null=True)
    inventory_on_hand = models.IntegerField(default=0)
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)

    class Meta:
        db_table = 'products'


class OrderConfirmation(models.Model):
    confirmation_code = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    customer_name = models.CharField(max_length=255, blank=True, null=True)
    customer_email  = models.CharField(max_length=255, blank=True, null=True)
    customer_phone  = JSONField(blank=True, null=True)
    purchase_products  = JSONField(blank=True, null=True)
    order_total = models.IntegerField(default=0)
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)

    class Meta:
        db_table = 'order_confirmation'

class OrderCreate(models.Model):
    order_create_id = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    #product = models.ForeignKey(Products, models.DO_NOTHING, blank=True, null=True)
    customer_name = models.CharField(max_length=255, blank=True, null=True)
    customer_email  = models.CharField(max_length=255, blank=True, null=True)
    customer_phone  = JSONField(blank=True, null=True)
    shipping_address  = JSONField(blank=True, null=True)
    billing_address  = JSONField(blank=True, null=True)
    purchase_products  = JSONField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)

    class Meta:
        db_table = 'order_create'


class ProductDetails(models.Model):
    product_details_id = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    product = models.ForeignKey(Products, models.DO_NOTHING, blank=True, null=True)
    product_type = JSONField(blank=True, null=True)
    category = JSONField(blank=True, null=True)
    pushed_product = models.BooleanField(default=False)
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)

    class Meta:
        db_table = 'product_details'














