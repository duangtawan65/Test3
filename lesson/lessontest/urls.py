from django.urls import path,include
from .views import *

urlpatterns = [
    path('',course_list,name='course_list'),
    
]
