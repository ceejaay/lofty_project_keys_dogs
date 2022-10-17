import time
import json
import logging

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.db import IntegrityError, transaction


from rest_framework import viewsets
from rest_framework.response import Response

from keys.serializers import KeySerializer
from keys.models import Key
from .tasks import create_key

class KeyViewSet(viewsets.ModelViewSet):
    queryset = Key.objects.all()

    def get_serializer_class(self):
        return KeySerializer

    def keys(self, request):
        if request.method == 'GET':
            all_keys = Key.objects.all()
            serializer_class = KeySerializer(all_keys, many=True)

            return Response(serializer_class.data)

        #create key
        if request.method == 'POST':
            body = json.loads(request.body)
            celery_key = create_key.delay(body)
            print(celery_key.request)
            print(celery_key.name)
            print(celery_key.backend)
            try:
                return celery_key
            except:
                Response({'status': 200, 'message': "Thank you.  Your request is processing"})
        Response({"hello": "world"})


    def key_detail(self, request, pk):
        body = json.loads(request.body)
        update_key.delay(body['value'])


        #get or 404
        if request.method == "GET":
            serialized = KeySerializer(single_key)
            return Response(serialized.data)

        if request.method == 'PUT':
            if body.get('value') is not None:
                update_key(body, single_key.value)
                single_key.value = int(body['value']) + int(single_key.value)
                single_key.save()
                serialized = KeySerializer(single_key)
                return Response(serialized.data, status=201)
            else:
                return Response({
                    "status": 400,
                    'message': {"new value missing"}
                    })



