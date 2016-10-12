from rest_framework import serializers
from post.models import Post

class PostSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.pk')
    likes_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()

    class Meta:
        model = Post
        fields = ('pk', 'user', 'title', 'created_at', 'updated_at', 'text',
                  'attachments', 'likes_count', 'comments_count')
