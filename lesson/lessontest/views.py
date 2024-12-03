from django.shortcuts import render
from .models import *

# Create your views here.
def course_list(request):
    cl = course.objects.all()
    return render(request,'course_list.html',{'cl':cl})
