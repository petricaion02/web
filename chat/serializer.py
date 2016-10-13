from rest_framework import serializers
from chat.models import Chat, Message


class ChatSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()

    class Meta:
        model = Chat
        fields = ('id', 'author', 'title', 'created_at', 'updated_at', 'users')

    def validate(self, data):
        user = self.context['request'].user.profile
        if user in data['users']:
            return data
        raise serializers.ValidationError("User %s not in chat %s"
            % (user, data['title']))



class MessageSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()

    class Meta:
        model = Message
        fields = ('id', 'author', 'text', 'created_at', 'chat')

    def validate(self, data):
        user = self.context['request'].user.profile
        if user in data['chat'].users.all():
            return data
        raise serializers.ValidationError("User %s not in chat %s"
            % (user, data['chat'].title))
