import os
import io
from rest_framework import permissions, status
from rest_framework.decorators import (api_view, permission_classes,
                                       renderer_classes)
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from django_rest_api.models import Products, ProductDetails, OrderCreate, OrderConfirmation
from django_rest_api.serializers import ProductsSerializer, ProductDetailsSerializer, OrderCreateSerializer
from django.shortcuts import get_object_or_404, get_list_or_404
from .data import createProducts, createProductsDetail, createOrderCreate


try:
    import ujson as json
except:
    import json

"""
JUST FOR DEMO TO ADD FAKER PRODUCT
"""
@api_view(['GET'])
@renderer_classes([JSONRenderer])
@permission_classes((permissions.AllowAny,))
def api_faker_product(request, product_id=None):
    """ GET product individual data
    """

    createProducts()
    createProductsDetail()
    createOrderCreate()
    return Response({"success": "data saved"}, status=status.HTTP_200_OK)

@api_view(['GET', 'POST'])
@renderer_classes([JSONRenderer])
@permission_classes((permissions.AllowAny,))
def api_products_list(request):
    """ GET products list data
        POST new product
    """
    if request.method == 'POST':
        if 'name' not in request.data:
            return Response('name is required', status=status.HTTP_417_EXPECTATION_FAILED)
        if 'code' not in request.data:
            return Response('code is required', status=status.HTTP_417_EXPECTATION_FAILED)
        if 'cost' not in request.data:
            return Response('cost is required', status=status.HTTP_417_EXPECTATION_FAILED)
        if 'description' not in request.data:
            return Response('description is required', status=status.HTTP_417_EXPECTATION_FAILED)
        if 'inventory_on_hand' not in request.data:
            return Response('inventory_on_hand is required', status=status.HTTP_417_EXPECTATION_FAILED)

        obj = Products.objects.create(**request.data)
        return Response({"success": "true", "product_code": obj.code}, status=status.HTTP_200_OK)
    else:
        products_list = ProductsSerializer(Products.objects.all(), many=True).data
        return Response({"data": products_list}, status=status.HTTP_200_OK)


@api_view(['GET'])
@renderer_classes([JSONRenderer])
@permission_classes((permissions.AllowAny,))
def api_product_individual(request, product_id=None):
    """ GET product individual data
    """

    product = ProductsSerializer(get_object_or_404(Products, pk=product_id))
    return Response({"data": product.data}, status=status.HTTP_200_OK)

@api_view(['GET'])
@renderer_classes([JSONRenderer])
@permission_classes((permissions.AllowAny,))
def api_products_details(request, product_id=None):
    """ GET products_details by product_id
    """
    product = get_object_or_404(Products, pk=product_id)
    product_details = ProductDetailsSerializer(get_list_or_404(ProductDetails, product=product), many=True)
    return Response({"product_details": product_details.data }, status=status.HTTP_200_OK)

@api_view(['POST'])
@renderer_classes([JSONRenderer])
@permission_classes((permissions.AllowAny,))
def api_add_products_details(request, product_id=None):
    """ Added products_details
    """
    if request.data == {}:
        return Response('No data in POST', status=status.HTTP_417_EXPECTATION_FAILED)

    if isinstance(request.data, list):
        for item in request.data:
            code = item['code']
            product = get_object_or_404(Products, pk=code)
            ProductDetails.objects.create(product=product, product_type=item['product_type'], category=item['category'], pushed_product=item['pushed_product'])
    else:

        product = get_object_or_404(Products, pk=int(request.data['code']))
        ProductDetails.objects.create(product=product, product_type=request.data['product_type'], category=request.data['category'], pushed_product=request.data['pushed_product'])
    return Response({"success": "true"}, status=status.HTTP_200_OK)

# @api_view(['GET'])
# @renderer_classes([JSONRenderer])
# @permission_classes((permissions.AllowAny,))
# def api_products_purchase_by_product_id(request, product_id=None):
#     """ GET products_purchase by product_id
#     """
#     product = get_object_or_404(Products, pk=product_id)
#     product_purchase = OrderCreateSerializer(get_list_or_404(OrderCreate, purchase_products__0__code=product.code), many=True)
#     return Response({"product_purchase": product_purchase.data }, status=status.HTTP_200_OK)

@api_view(['POST'])
@renderer_classes([JSONRenderer])
@permission_classes((permissions.AllowAny,))
def api_products_purchase(request, product_id=None):
    """ POST products_purchase by product_id
    """
    if request.data == {}:
        return Response('No data in POST', status=status.HTTP_417_EXPECTATION_FAILED)

    if request.method == 'POST':

        if isinstance(request.data, list):
            for item in request.data:
                if 'customer_name' not in item:
                    return Response('customer_name is required', status=status.HTTP_417_EXPECTATION_FAILED)
                if 'customer_email' not in item:
                    return Response('customer_email is required', status=status.HTTP_417_EXPECTATION_FAILED)
                if 'customer_phone' not in item:
                    return Response('customer_phone is required', status=status.HTTP_417_EXPECTATION_FAILED)
                if 'shipping_address' not in item:
                    return Response('shipping_address is required', status=status.HTTP_417_EXPECTATION_FAILED)

                if 'billing_address' not in item:
                    return Response('billing_address is required', status=status.HTTP_417_EXPECTATION_FAILED)
                if 'purchase_products' not in item:
                    return Response('purchase_products is required', status=status.HTTP_417_EXPECTATION_FAILED)
                elOrder = {'customer_name': item['customer_name'], 'customer_email': item['customer_email'],
                      'customer_phone': item['customer_phone'], 'shipping_address': item['shipping_address'],
                      'billing_address': item['billing_address'], 'purchase_products': item['purchase_products']}

                elOrderConf = {'customer_name': item['customer_name'], 'customer_email': item['customer_email'],
                                'customer_phone': item['customer_phone'],'order_total': item['order_total'],
                                'purchase_products': item['purchase_products']}
                product = get_object_or_404(Products, pk=product_id)
                order = OrderCreate.objects.create(**elOrder, product=product)
                OrderConfirmation.objects.create(**elOrderConf, order_create=order)
        else:
            elOrder = {'customer_name': request.data['customer_name'], 'customer_email': request.data['customer_email'],
                    'customer_phone': request.data['customer_phone'], 'shipping_address': request.data['shipping_address'],
                    'billing_address': request.data['billing_address'], 'purchase_products': request.data['purchase_products']}

            elOrderConf = {'customer_name': request.data['customer_name'], 'customer_email': request.data['customer_email'],
                            'customer_phone': request.data['customer_phone'],'order_total': request.data['order_total'],
                            'purchase_products': request.data['purchase_products']}
            product = get_object_or_404(Products, pk=product_id)
            order = OrderCreate.objects.create(**elOrder, product=product)
            OrderConfirmation.objects.create(**elOrderConf, order_create=order)
    return Response({"success": "created"}, status=status.HTTP_200_OK)


@api_view(['POST'])
@renderer_classes([JSONRenderer])
@permission_classes((permissions.AllowAny,))
def api_products_order_confirmation(request):
    """ Added order confirmation
    """
    if request.data == {}:
        return Response('No data in POST', status=status.HTTP_417_EXPECTATION_FAILED)

    if request.method == 'POST':
        if 'customer_name' not in request.data:
            return Response('customer_name is required', status=status.HTTP_417_EXPECTATION_FAILED)
        if 'customer_email' not in request.data:
            return Response('customer_email is required', status=status.HTTP_417_EXPECTATION_FAILED)
        if 'customer_phone' not in request.data:
            return Response('customer_phone is required', status=status.HTTP_417_EXPECTATION_FAILED)
        if 'purchase_products' not in request.data:
            return Response('purchase_products is required', status=status.HTTP_417_EXPECTATION_FAILED)
        if 'order_total' not in request.data:
            return Response('order_total is required', status=status.HTTP_417_EXPECTATION_FAILED)

        for pp in request.data['purchase_products']:
            code = pp['code']
            get_object_or_404(Products, pk=code)
            OrderConfirmation.objects.create(**request.data)
    return Response({"success": "created"}, status=status.HTTP_200_OK)
