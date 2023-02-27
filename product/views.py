from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from.models import CartItem
from .serializers import ProductSerializer 
from .serializers import CartItemSerializer
from rest_framework.views import APIView



@api_view(['GET'])
def search(request):
        query = request.GET.get('q')
        if query:
            products = Product.objects.filter(name__icontains=query) | \
                    Product.objects.filter(description__icontains=query) 
        else:
            products = Product.objects.all()

        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def ring(request):
    rings = Product.objects.all().filter(name__contain="Ring")
    serializer = ProductSerializer(rings, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def products(request):
 
    if request.method == 'GET': # list products
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    elif request.method == 'POST': # create new product
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

@api_view(['GET'])
def product(request,pk):
     if request.method == 'GET': # list products
        product = Product.pk()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

@api_view(['GET','PUT'])
def single_product(request, pk):
    if request.method == 'GET':
        single_product = Product.objects.get(id=pk)
        serializer = ProductSerializer(single_product, many=False) 
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProductSerializer(single_product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

@api_view(['GET', 'POST'])
def items(request):
    
    if request.method == 'GET':  
        items = CartItem.objects.all()
        serializer = CartItemSerializer (items, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST': # add item ( add product to cart)
        try:
            productId = request.data.get('productId')
            product = Product.objects.get(id=productId)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
        
        quantity = request.data.get('quantity')
        cart_item, created = CartItem.objects.get_or_create( product=product)
        if not created:
            cart_item.quantity += int(quantity)    
        else:
            cart_item.quantity = int(quantity)           
        cart_item.save()
        return Response(status=status.HTTP_201_CREATED)
            


@api_view(['GET','PUT'])
def single_cart_item(request, pk):
    if request.method == 'GET':
        single_item_in_cart = CartItem.objects.get(id=pk)
        serializer = CartItemSerializer(single_item_in_cart, many=False) 
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CartItemSerializer(single_item_in_cart, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'DELETE', 'GET'])
def single_item(request, pk) :
    
    try: 
        
        cart_item = CartItem.objects.get(id=pk) 
        
    except CartItem.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    
    if request.method == 'GET' :   # get single item (product in cart)
        serializer = CartItemSerializer(cart_item, many=False)
        return Response(serializer.data)
    
    
    if request.method == 'DELETE': # delete item
       cart_item.delete()
       return Response(status=status.HTTP_204_NO_CONTENT)
           
           
    if request.method == 'PUT' :  # update item (quantity) in cart 
        quantity = request.data.get('quantity')
        cart_item.quantity = int(quantity)
        cart_item.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
