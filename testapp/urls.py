from django.urls import path

from .views import *

urlpatterns = [    
    path('test0/', Test0View.as_view()),
    path('test1/', test1),
    path('test2/', Test2View.as_view()),
    path('setc/', set_c),
    path('getc/', get_c),
    path('test3/', test3),
    path('test4/', test4),
    path('test5/', test5),
    path('sessiontest/', session_test),
    path('test6/', Test6View.as_view()),
    path('test7/', test7),
    path('test8/', test8),
    path('test9/', test9, name = 'test9'),
]