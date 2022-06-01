import requests
import json
import time
import datetime

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView

from .models import *
from .serializers import *

# Create your views here.


#--test--test--test--test--test--test--test--test--test--test--test--test--test--test--test--test--test

print('igc1')

class IGC0View(APIView):
    def get(self,request):
        # try:            
        #     pet = Pet.objects.get(id = 2).owner.create(
        #         name = '名',
        #         nickname = '小名',
        #         gender = 1,
        #         birth_date = datetime.strptime('20100101','%Y%m%d').date(),
        #         species = 'dog',
        #     )
        # except Exception as e:
        #     return Response(e)
        return Response('hi')


class IGC1View(APIView):
    def post(self, request):
        print(request.data)
        data = request.data
        serializer = CustomerSerializer(data = data)
        if not serializer.is_valid():
            res = {'message': '驗證沒過'}
            return Response(res)
        data = serializer.validated_data
        customer = Customer.objects.create(**data)
        res = {'message': '創建成功'}
        return Response(res)

class IGC2View(APIView):
    '''
    pet創建
    '''
    def post(self, request):
        print(request.data)
        data = request.data
        serializer = CustomerSerializer(data = data)
        if not serializer.is_valid():
            res = {'message': '驗證沒過'}
            return Response(res)
        data = serializer.validated_data
        pet_owner, created = Customer.objects.get_or_create(

        )
        pet = Pet.objects.create(
            name = data.get('name'),
            nickname = data.get('nickname'),
            owner = pet_owner,
            gender = data.get('gender'),
            birth_date = data.get('birth_date'),
            species = data.get('species'),
        )
        res = {'message': '創建成功'}
        return Response(res)