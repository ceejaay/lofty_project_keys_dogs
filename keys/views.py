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
# from .tasks import get_key
# transaction.on_commit(lambda: get_key.delay(pk=103))
# Create your views here.

logger = logging.getLogger(__name__)


class KeyViewSet(viewsets.ModelViewSet):
    queryset = Key.objects.all()

    def get_serializer_class(self):
        return KeySerializer

    def keys(self, request):
        #get all keys
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
            new_key = Key()

            if body.get('key') is not None:
                new_key.key = body['key']
            else:
                return Response({'status': 400, 'message': "Must include key"})

            if body.get('value') is not None:
                new_key.value = body['value']

            try:
                new_key.save()
            except IntegrityError as  e:
                return Response({'status': 400, 'message': f"{e}"})

            serialized = KeySerializer(new_key)
            create_end_time = time.time()
            logger.info(f"CREATE TIME { create_end_time - create_start_time }")
            if create_end_time - create_start_time >=10:
                logger.warning(f"Create time exceeds 10 {create_end_time - create_start_time}")
            return Response(serialized.data)

    def key_detail(self, request, pk):
        start_time = time.time()
        single_key = get_object_or_404(Key, pk=pk)
        body = json.loads(request.body)

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



