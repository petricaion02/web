from django.shortcuts import render
from rest_framework import generics, serializers
from chat.serializer import ChatSerializer, MessageSerializer
from chat.models import Chat, Message
# Create your views here.
from rest_framework import permissions
from rest_framework import viewsets
from application.permissions import IsAuthorOrReadOnly
from chat.permissions import IsInChatMessage, IsInChat
from user.models import FriendShip, UserProfile
from oauth2_provider.ext.rest_framework import TokenHasResourceScope
import operator


def chats(request):
    return render(request=request, template_name='chat/chats.html')

def chat(request, pk):
    return render(request, 'chat/chat.html', {'pk': pk})

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    required_scopes = ['chat']
    permission_classes = (permissions.IsAuthenticated, IsAuthorOrReadOnly,
                          IsInChatMessage, TokenHasResourceScope)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user.profile)

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(chat__users__in=[self.request.user.profile])
        chat_id = self.request.query_params.get('chat')
        if chat_id:
            qs = qs.filter(chat__pk=chat_id)
        message_id = self.request.query_params.get('id')
        if message_id:
            qs = qs.filter(pk=message_id)
        return qs


class ChatViewSet(viewsets.ModelViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    required_scopes = ['chat']
    permission_classes = (permissions.IsAuthenticated, IsInChat,
                          IsAuthorOrReadOnly, TokenHasResourceScope)

    def perform_create(self, serializer):
        author = self.request.user.profile
        users = self.request._data.getlist('users')
        for user in users:
            profile = UserProfile.objects.get(pk=user)

            if not (FriendShip.objects.filter(first_user__id=user, second_user=author).count()):
                raise serializers.ValidationError("%s is not a friend/follower of %s"
                    % (profile.user.username, author.user.username))

        serializer.save(author=self.request.user.profile)

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(users__in=[self.request.user.profile])
        chat_id = self.request.query_params.get('id')
        if chat_id:
            qs = qs.filter(pk=chat_id)
        return qs
