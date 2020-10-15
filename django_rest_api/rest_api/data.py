from django_rest_api.models import Products, ProductDetails, OrderCreate
from django.shortcuts import get_object_or_404, get_list_or_404

def createProducts():
    p = [{
      "name": "product 01",
      "code": 300,
      "cost": 30,
      "description": "added new prodcut 303",
      "inventory_on_hand": 2
        },
        {
      "name": "product 01",
      "code": 301,
      "cost": 30,
      "description": "added new prodcut 301",
      "inventory_on_hand": 9
        },
        {
      "name": "product 01",
      "code": 302,
      "cost": 32,
      "description": "added new prodcut 302",
      "inventory_on_hand": 12
        }]
    for item in p:
        Products.objects.create(**item)
def createProductsDetail():
    pd = [{
      "name": "demo1",
      "code": 300,
      "product_type": {
        "type_name": "pariatur",
        "type": "cillum officia non dolor"
      },
      "cost": 20978825,
      "description": "demo1 description",
      "pushed_product": False,
      "callback": "magna sed",
      "category": {
        "name": "categ 1",
        "type": "nostrud non veniam"
      }
    },
    {
        "name": "[object Object]",
        "code": 301,
        "product_type": {
            "type_name": "pariatur",
            "type": "cillum officia non dolor"
        },
        "cost": 20978825,
        "description": "[object Object]",
        "pushed_product": True,
        "callback": "magna sed",
        "category": {
            "name": "[object Object]",
            "type": "nostrud non veniam"
        }
    }]

    for item in pd:
        product = get_object_or_404(Products, pk=item['code'])
        ProductDetails.objects.create(product=product, product_type=item['product_type'], category=item['category'], pushed_product=item['pushed_product'])

# def createOrderCreate():
#     i = 301
#     oc=[
#         {
#                 "customer_name": "aute",
#                 "customer_email": "culpa dolor laborum incididunt",
#                 "customer_phone": [
#                     {
#                     "number": 18953712,
#                     "type": "voluptate sunt consequat aliqua occaecat",
#                     "contact": True
#                     },
#                     {
#                     "number": 46388657,
#                     "type": "quis",
#                     "contact": True
#                     }
#                 ],
#                 "shipping_address": [
#                     {
#                     "street": "Excepteur in id est irure",
#                     "city": "sit anim sint tempor",
#                     "state": "incididunt aliqua",
#                     "zipcode": 96878743
#                     }
#                 ],
#                 "billing_address": [
#                     {
#                     "street": "amet dolor ut do consectetur",
#                     "city": "deserunt eiusmod ullamco",
#                     "state": "in irure nisi Excepteur",
#                     "zipcode": 81798561
#                     },
#                     {
#                     "street": "nulla velit voluptate pariatur",
#                     "city": "dolor amet",
#                     "state": "esse dolor labore",
#                     "zipcode": 18729617
#                     },
#                     {
#                     "street": "dolore laboris sint commodo dolor",
#                     "city": "Duis",
#                     "state": "fugiat dolore elit commodo",
#                     "zipcode": -41344223
#                     }
#                 ],
#                 "purchase_products": [
#                     {
#                     "code": 91001861,
#                     "quantity": -67325778
#                     },
#                     {
#                     "code": 69406482,
#                     "quantity": -6735510
#                     }
#                 ]
#             },
#         {
#                 "customer_name": "aute",
#                 "customer_email": "culpa dolor laborum incididunt",
#                 "customer_phone": [
#                     {
#                     "number": 18953712,
#                     "type": "voluptate sunt consequat aliqua occaecat",
#                     "contact": False
#                     },
#                     {
#                     "number": 46388657,
#                     "type": "quis",
#                     "contact": True
#                     }
#                 ],
#                 "shipping_address": [
#                     {
#                     "street": "Excepteur in id est irure",
#                     "city": "sit anim sint tempor",
#                     "state": "incididunt aliqua",
#                     "zipcode": 96878743
#                     }
#                 ],
#                 "billing_address": [
#                     {
#                     "street": "amet dolor ut do consectetur",
#                     "city": "deserunt eiusmod ullamco",
#                     "state": "in irure nisi Excepteur",
#                     "zipcode": 81798561
#                     },
#                     {
#                     "street": "nulla velit voluptate pariatur",
#                     "city": "dolor amet",
#                     "state": "esse dolor labore",
#                     "zipcode": 18729617
#                     },
#                     {
#                     "street": "dolore laboris sint commodo dolor",
#                     "city": "Duis",
#                     "state": "fugiat dolore elit commodo",
#                     "zipcode": -41344223
#                     }
#                 ],
#                 "purchase_products": [
#                     {
#                     "code": 91001861,
#                     "quantity": -67325778
#                     },
#                     {
#                     "code": 69406482,
#                     "quantity": -6735510
#                     }
#                 ]
#     }]


#     for item in oc:
#         product = get_object_or_404(Products, pk=i)
#         OrderCreate.objects.create(**item, product=product)
#         i = i + 1
