# Generated by Django 3.0.5 on 2020-10-14 18:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_rest_api', '0002_remove_productdetails_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordercreate',
            name='product',
        ),
        migrations.AddField(
            model_name='productdetails',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='django_rest_api.Products'),
        ),
    ]