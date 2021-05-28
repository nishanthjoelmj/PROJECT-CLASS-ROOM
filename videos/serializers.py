from rest_framework import serializers
from .models import FileUpload,Marks
from django.apps import apps
Events=apps.get_model('Event','Event')

class MarksSerializer(serializers.ModelSerializer) :
    class Meta:
        model=Marks
        #fields="__all__"
        fields=('video_link','date','by_email','EventName','marks')

class videoUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model= FileUpload
        #fields="__all__"
        fields=('url_64encoding','date','username',)

class videoUploadSerializerMark(serializers.ModelSerializer):
    class Meta:
        model= FileUpload
        #fields="__all__"
        fields=('url_64encoding','date','username','EventName')

class SubmitVideo(serializers.ModelSerializer) :

    class Meta :
        model=FileUpload
        fields=('video','captions')
        #extra_kwargs = {'username': {'required': False}}

class VDContent(serializers.ModelSerializer):

    class Meta:
        model= FileUpload
        fields=('url_64encoding','captions','username','date','EventName')

class EventSerial(serializers.ModelSerializer):

    class Meta:
        model=Events
        fields='__all__'