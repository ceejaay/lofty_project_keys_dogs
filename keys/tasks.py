from keys.models import Key
from celery import shared_task


@shared_task
def add(x, y):
    return x + y

@shared_task()
def create_key(key_object):
    new_key = Key()
    if key_object.get('key') is not None:
        new_key.key = key_object['key']
    else:
        return Response({'status': 400, 'message': "Must include key"})

    if body.get('value') is not None:
        new_key.value = body['value']

    try:
        print(">>>>>>>>>>>>> Saving key >>>>>>>>>>>>>")
        new_key.save()
    except IntegrityError as  e:
        print(">>>>>>>>>>>>>>> Error", e)
        return Response({'status': 400, 'message': f"{e}"})


