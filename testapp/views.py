import requests
import json
import time
import random

from datetime import datetime

from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.core import serializers
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django import forms
from django.contrib.sessions.models import Session

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView

from faker import Faker

from .models import *
from app0.models import *
from .serializers import *
from test import *

# Create your views here.


#--test--test--test--test--test--test--test--test--test--test--test--test--test--test--test--test--test


class Test0View(APIView):
    def get(self,request):
        dic = {
            'a':'a',
            'b':2,
            'c':[
                {
                    'd':'d',
                    'e':'e'
                },
                {
                    'd':'d2',
                    'e':'e2'
                }
            ]
        }
        print(type(dic['c']))
        return Response(dic)

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
        owner_cnt = Owner.objects.all().count()
        print(owner_cnt)
        if owner_cnt == 0:
            return Response('沒有主人可選')

        
        while True:
            id = random.randint(1,owner_cnt)
            try:
                owner = Owner.objects.get(id = id)
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

        
class Test3View(APIView):
    def get(self,request):
        return Response('only test')


def set_c(request):
    response = HttpResponse('Set your lucky_number as 8')
    response.set_cookie('sessionid', 'lcdp9xx6vjtrrohy7bigr54lrxxhakmo')
    return response


def get_c(request):
    if 'lucky_number' in request.COOKIES:
        return HttpResponse('Your lucky_number is {0}'.format(request.COOKIES['lucky_number']))
    else:
        return HttpResponse('No cookies.') 

#測試在 response 的 headers 裡面添加東西
def test3(request):
    response = HttpResponse('test set response')
    response.headers['test'] = 'you find me'
    return response

#測試 讀取 response
def test4(request):
    payload = json.dumps({
        'msg': 'hi'
    })
    response = requests.request('GET',
        'http://10.66.200.52:9527/testapp/test3/',
        headers = {'Content-Type': 'application/json'},
        data = payload,
    )
    if response.status_code != 200:
        return HttpResponse('not 200')
    return HttpResponse(response.headers['test'])


class Count(object):
    num = 0
    def count():
        Count.num += 1
        return Count.num


def test5(request):
    for i in range(10):
        # 電子郵件內容樣板
        num = Count.count()
        email_template = render_to_string(
            'signup.html',
            {"data": f"這是第{num}封信"}
        )
        email = EmailMessage(
            f'成功通知信{num}',  # 電子郵件標題
            email_template,  # 電子郵件內容
            settings.EMAIL_HOST_USER,  # 寄件者
            ['xoxakes320@krunsea.com']  # 收件者
        )
        email.fail_silently = False
        email.send()
        print(num)
    return HttpResponse('已寄信')

def session_test(request):
    sid = request.COOKIES['sessionid']
    s = Session.objects.get(pk=sid)
    s_info = 'Session ID:' + sid +\
         '<br>Expire_date:' + str(s.expire_date) + \
             '<br>Data:' + str(s.get_decoded())
    return HttpResponse(s_info)


class Test6View(APIView):
    def get(self,request):
        return Response(status = 404)


def test7(request):
    response = HttpResponseRedirect('/testapp/test8')
    response.headers['data'] = 'canCarry'
    return response

def test8(request):
    # request.headers['data'] = 'whatThe'
    return HttpResponse(f'讀取到的資料是\
        <br><br><br><br><br>{request.headers.keys()}')
