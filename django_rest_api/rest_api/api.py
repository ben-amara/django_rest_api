import os
import io
from rest_framework import permissions, status
from rest_framework.decorators import (api_view, permission_classes,
                                       renderer_classes)
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from django_rest_api.models import Products, ProductDetails, OrderCreate
from django_rest_api.serializers import ProductsSerializer, ProductDetailsSerializer
from django.shortcuts import get_object_or_404, get_list_or_404


try:
    import ujson as json
except:
    import json

@api_view(['GET', 'POST'])
@renderer_classes([JSONRenderer])
@permission_classes((permissions.AllowAny,))
def api_products_list(request):
    """ GET products list data
        POST new product
    """
    if request.method == 'POST':
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

    product_details = ProductDetailsSerializer(get_list_or_404(ProductDetails, product=product_id))
    return Response({"product_details": product_details.data }, status=status.HTTP_200_OK)

@api_view(['POST'])
@renderer_classes([JSONRenderer])
@permission_classes((permissions.AllowAny,))
def api_products_purchase(request, product_id=None):
    """ POST products_purchase by product_id
    """
    if request.data == {}:
        return Response('No data in POST', status=status.HTTP_417_EXPECTATION_FAILED)

    if request.method == 'POST':
        product = get_object_or_404(Products, pk=product_id)
        obj = OrderCreate.objects.create(**request.data, product=product)
        return Response({"success": "true", "order_create_id": obj.order_create_id}, status=status.HTTP_200_OK)
