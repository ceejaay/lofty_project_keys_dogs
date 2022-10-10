from keys.models import Key 
from rest_framework import serializers

class KeySerializer(serializers.ModelSerializer):
    class Meta:
        model = Key 
        fields = ['id', 'key', 'value']

