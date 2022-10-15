from keys.models import Key
from lofty_app.celery import app
from celery import Celery, shared_task
from django.db import IntegrityError, transaction
from rest_framework.response import Response
import time
import random


@shared_task
def add(x, y):
    return x + y

@app.task()
def create_key(key_object):
    # time.sleep(random.randint(0, 30))
    new_key = Key()
    if key_object.get('key') is not None:
        new_key.key = key_object['key']
    else:
        return Response({'status': 400, 'message': "Must include key"})

    if key_object.get('value') is not None:
        new_key.value = key_object['value']

    try:
        new_key.save()
        return {'key': new_key.key, 'value': new_key.value, 'status': 200}
    except IntegrityError as  e:
        return {'status': 400, 'message': f"{e}"}


