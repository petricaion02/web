from rest_framework import serializers
from image.models import Image
from application import settings

class ImageSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.pk')
    url = serializers.SerializerMethodField()

    def get_url(self, obj):
        return obj.file.url

    likes_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()

    class Meta:
        model = Image
        fields = ('pk', 'user', 'created_at', 'updated_at', 'url',
                  'likes_count', 'comments_count')
