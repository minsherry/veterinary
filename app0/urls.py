from django.urls import path

from .views import *

urlpatterns = [    
    path('igc0/', IGC0View.as_view()),
    path('igc1/', IGC1View.as_view()),
    path('igc2/', IGC2View.as_view()),
]