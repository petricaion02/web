from rest_framework import serializers
from like.models import Like
from abstract.serializer import GenericRelationsModelSerializer
from django.contrib.contenttypes.models import ContentType


class LikeSerializer(GenericRelationsModelSerializer):
    user = serializers.ReadOnlyField(source='user.pk')

    class Meta:
        model = Like
        fields = ('pk', 'item_type', 'item_id', 'user', 'created_at')
