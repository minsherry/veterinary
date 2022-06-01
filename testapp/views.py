import requests
import json
import time
import random

from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.core import serializers

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView

from faker import Faker

from .models import *
from app0.models import *
from .serializers import *

# Create your views here.


#--test--test--test--test--test--test--test--test--test--test--test--test--test--test--test--test--test


class Test0View(APIView):
    def get(self,request):     
        '''
        自動產生變數去新增顧客
        '''   
        faker = Faker('zh-TW')
        
        for i in range(11):
            ph_no=[]
            ph_no.append(0)
            ph_no.append(9)
            for i in range(8):
                ph_no.append(random.randint(0,9))
            ph = ''.join(str(e) for e in ph_no)

            Customer.objects.create(
                first_name = faker.first_name(),
                last_name = faker.last_name(),
                birth_date = datetime.strptime(faker.date(), "%Y-%m-%d"),
                phone = ph,
                email = faker.ascii_free_email(),
                address = faker.address()
            )
        return Response('over')

    def post(self, request):
        data = request.data
        serializer = TestSerializer(data = data)
        if not serializer.is_valid():
            return Response(f'失敗{serializer.error_messages}')
        
        data = serializer.validated_data
        # return Response(f"{data}")
        try:
            #以下成功
            # f = Food(
            #         name = data.get('food').get('name'),
            #         number = data.get('food').get('number')
            #     )
            # f.save()
            # c = Combo(
            #     food = f,
            #     cost = data.get('cost')
            # )
            # c.save()

            #以下成功
            c = Combo(
                food = Food(
                    name = data.get('food').get('name'),
                    number = data.get('food').get('number')
                ),
                cost = data.get('cost')
            )
            c.food.save()
            c.save()
            
            #以下成功
            # combo = Combo.objects.create(
            #     food = Food.objects.create(
            #         name = data.get('food').get('name'),
            #         number = data.get('food').get('number')
            #     ),
            #     cost = data.get('cost')
            # )
        except Exception as e:
            return Response(f'新增失敗 原因是:{e}')

        return Response(f'成功{data}')


def test1(request):
    a = Food(name = 'cow', number = 5)
    a.save()
    return HttpResponse('yes')

    
class Test2View(APIView):
    def get(self,request):     
        '''
        自動產生變數去新增顧客
        '''   
        faker = Faker('zh-TW')


        #判斷主人
        owner_cnt = Customer.objects.all().count()
        print(owner_cnt)
        if owner_cnt == 0:
            return Response('沒有主人可選')

        
        while True:
            id = random.randint(1,owner_cnt)
            try:
                owner = Customer.objects.get(id = id)
                break
            except:
                pass
        print('找到主人')

        #判斷寵物
        pet_cnt = Pet.objects.all().count()
        if pet_cnt ==0:
            return Response('沒有寵物可選')

        
        while True:
            id = random.randint(1,pet_cnt)
            try:
                pet = Pet.objects.get(id = id)
                break
            except:
                pass
        print('找到寵物')

        #判斷獸醫        
        veterinarys = Employee.objects.filter(job = 0)
        if veterinarys.count() == 0:
            return Response('沒有獸醫可選')
        id = random.randint(0, veterinarys.count()-1)
        veterinary = veterinarys[id]
        print(veterinary.last_name)
        print('找到獸醫')



        mr = MedicalRecord.objects.create(
            record_datetime = faker.date_time(),
            spend_time_in_minute = random.randint(1,100),
            pet = pet,
            veterinary = veterinary,
            detail = '',
        )


        return Response('over')