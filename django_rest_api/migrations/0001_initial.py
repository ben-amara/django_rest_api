# Generated by Django 3.0.5 on 2020-10-12 17:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('customer_name', models.CharField(blank=True, max_length=255, null=True)),
                ('customer_mail', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'db_table': 'customer',
            },
        ),
        migrations.CreateModel(
            name='CustomerPhone',
            fields=[
                ('customer_phone_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('contact', models.BooleanField(blank=True, default=True, null=True)),
                ('type_number', models.CharField(blank=True, max_length=255, null=True)),
                ('number', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='django_rest_api.Customer')),
            ],
            options={
                'db_table': 'customer_phone',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('code', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('cost', models.IntegerField(default=0)),
                ('description', models.TextField(blank=True, null=True)),
                ('inventory_on_hand', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'db_table': 'products',
            },
        ),
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('shipping_address_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('street', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('state', models.CharField(blank=True, max_length=255, null=True)),
                ('zipcode', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='django_rest_api.Customer')),
            ],
            options={
                'db_table': 'shipping_address',
            },
        ),
        migrations.CreateModel(
            name='PurchaseProducts',
            fields=[
                ('purchase_products_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('quantity', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('code', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='django_rest_api.Products')),
            ],
            options={
                'db_table': 'purchase_products',
            },
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('product_type_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('type_name', models.CharField(blank=True, max_length=255, null=True)),
                ('type_product', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='django_rest_api.Products')),
            ],
            options={
                'db_table': 'product_type',
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('product_category_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('type_category', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='django_rest_api.Products')),
            ],
            options={
                'db_table': 'product_category',
            },
        ),
        migrations.CreateModel(
            name='OrderConfirmation',
            fields=[
                ('order_confirmation_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('order_confirmation', models.CharField(blank=True, max_length=255, null=True)),
                ('order_total', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('customer_phone', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='django_rest_api.CustomerPhone')),
                ('purchase_products', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='django_rest_api.PurchaseProducts')),
            ],
            options={
                'db_table': 'order_confirmation',
            },
        ),
        migrations.CreateModel(
            name='BillingAddress',
            fields=[
                ('shipping_address_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('street', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('state', models.CharField(blank=True, max_length=255, null=True)),
                ('zipcode', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='django_rest_api.Customer')),
            ],
            options={
                'db_table': 'billing_address',
            },
        ),
    ]
