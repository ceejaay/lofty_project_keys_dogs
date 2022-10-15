import time
import json
import logging

from django.shortcuts import render
from django.http import HttpResponse
from django.db import IntegrityError, transaction


from rest_framework import viewsets
from rest_framework.response import Response

from keys.serializers import KeySerializer
from keys.models import Key
from .tasks import create_key
from lofty_app.celery import debug_task

logger = logging.getLogger(__name__)


class KeyViewSet(viewsets.ModelViewSet):
    queryset = Key.objects.all()

    def get_serializer_class(self):
        return KeySerializer

    def keys(self, request):
        start_time = time.time()
        if request.method == 'GET':
            all_keys = Key.objects.all()
            serializer_class = KeySerializer(all_keys, many=True)
            end_time = time.time()
            logger.info(f"GET ALL KEYS {end_time - start_time}")

            return Response(serializer_class.data)

        #create key
        if request.method == 'POST':
            create_start_time = time.time()
            body = json.loads(request.body)
            d = create_key(body)
            if d['status'] == 200:
                serialized = KeySerializer(d)
                return Response(serialized.data)
            else:
                return Response(d)

    def key_detail(self, request, pk):
        start_time = time.time()
        single_key = Key.objects.get(pk=pk)

        #get or 404
        if request.method == "GET":
            serialized = KeySerializer(single_key)
            end_time = time.time()
            logger.info(f"Get single Key- {end_time - start_time}")
            if end_time - start_time >= 10:
                logger.warning(f"Create time exceeds 10 {end_time - start_time}")
            return Response(serialized.data)

        if request.method == 'PUT':
            start_time = time.time()
            if body.get('value') is not None:
                single_key.value = int(body['value']) + int(single_key.value)
                single_key.save()
                serialized = KeySerializer(single_key)
                end_time = time.time()
                logger.info(f"PUT key - { end_time - start_time }")
                if end_time - start_time >=10:
                    logger.warning(f"Create time exceeds 10 {end_time - start_time}")
                return Response(serialized.data)

            else:
                return Response({
                    "status": 400,
                    'message': {"new value missing"}
                    })



