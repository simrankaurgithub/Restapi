from django.shortcuts import render
from .models import *
from .serializers import *

# Create your views here.
def test_api(request):
    stu=Student.objects.all()
    serializer = StudentSerializer(stu)
    