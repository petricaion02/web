from rest_framework import serializers
from comment.models import Comment
from abstract.serializer import GenericRelationsModelSerializer
from django.contrib.contenttypes.models import ContentType


class CommentSerializer(GenericRelationsModelSerializer):
    user = serializers.ReadOnlyField(source='user.pk')
    likes_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()

    class Meta:
        model = Comment
        fields = ('pk', 'item_type', 'item_id', 'user', 'text', 'created_at', 'updated_at',
                  'likes_count', 'comments_count')
