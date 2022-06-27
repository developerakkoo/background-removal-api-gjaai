from django.shortcuts import render
from rest_framework import viewsets
from .models import uploadimage
from .serializers import uploadimageserializer
from rembg import remove
from PIL import Image
import cv2

# Create your views here.

def bgRemove(filename):
    input = cv2.imread(filename)
    output = remove(input)
    cv2.imwrite("testbg.png",output)

class uploadimageView(viewsets.ModelViewSet):
    print("Run Image Processing here")
    queryset = uploadimage.objects.all()
    serializer_class = uploadimageserializer
