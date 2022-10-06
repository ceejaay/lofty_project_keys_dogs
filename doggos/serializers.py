from doggos.models import DogImage
from rest_framework import serializers

class DogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DogImage
        fields = ['url', 'duplicate_url', 'id', 'file_type', 'height', 'width', 'filename', 'preview_link']


