import os
import io
from rest_framework import permissions, status
from rest_framework.decorators import (api_view, permission_classes,
                                       renderer_classes)
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

try:
    import ujson as json
except:
    import json

@api_view(['POST'])
@renderer_classes([JSONRenderer])
@permission_classes((permissions.AllowAny,))
def api_order_confirmation(request):
    """ POST purchase_products data
    """
    return Response(request.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@renderer_classes([JSONRenderer])
@permission_classes((permissions.AllowAny,))
def api_order_create(request):
    """ POST order_create data
    """
    return Response(request.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@renderer_classes([JSONRenderer])
@permission_classes((permissions.AllowAny,))
def api_product_description(request, product_id=None):
    """ GET product_description by
    """

    return Response({'product_id': product_id}, status=status.HTTP_200_OK)

@api_view(['GET'])
@renderer_classes([JSONRenderer])
@permission_classes((permissions.AllowAny,))
def api_product_list(request, product_id=None):
    """ GET product_description by
    """
    return Response({'product_id': product_id}, status=status.HTTP_200_OK)
