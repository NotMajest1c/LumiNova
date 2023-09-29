from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
# Create your views here.

from django.contrib import messages
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import DataSerializer

from .models import product

def product_view(request):
    
    prod = [1,2,3]
    
    my_cont  = {
        "product" : prod,

    }
    
@api_view(['GET'])
def getProductData(request):
    app = product.objects.all()
    
    serializer = DataSerializer(app, many=True)
    return Response(serializer.data)

   


