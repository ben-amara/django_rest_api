# Generated by Django 3.0.5 on 2020-10-14 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_rest_api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productdetails',
            name='product',
        ),
    ]
