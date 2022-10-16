from django.test import TestCase
from rest_framework.test import APIClient, APITestCase


from keys.models import Key

class TestKeys(APITestCase):

    def setUp(self):
        self.key = Key.objects.create(
                key="test_value",
                value=10
                )
        self.client = APIClient()


    def test_for_new_key(self):
        r = self.client.post("/keys/", {'value': 55, 'key': 'some_new_Key'}, format='json')
        k = Key.objects.last()

        self.assertEqual(r.status_code, 200)
        self.assertEqual(k.key, 'some_new_Key')
        self.assertEqual(k.value, 55)

    def test_incremented_key(self):
        key = Key.objects.first()

        r = self.client.put(f'/keys/key_detail/{key.id}/', {'value': 1}, format='json')
        k = Key.objects.last()
        self.assertEqual(r.status_code, 201)
        self.assertEqual(k.value, 11)

    def test_missing_key(self):
        r = self.client.post('/keys/', {'value': 3}, format='json')
        self.assertEqual(r.status_code, 400)

