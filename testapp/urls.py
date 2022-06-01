from django.urls import path

from .views import *

urlpatterns = [    
    path('test0/', Test0View.as_view()),
    path('test1/', test1),
    path('test2/', Test2View.as_view()),
]