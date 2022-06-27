from rest_framework import serializers
from .models import uploadimage

class uploadimageserializer(serializers.HyperlinkedModelSerializer):
    class Meta :
        model = uploadimage
        fields =('title','images',)