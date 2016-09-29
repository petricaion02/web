from django.db import models

# Create your models here.

from abstract.models import CreatableModel, UpdatableModel
from user.models import UserProfile

class Message(CreatableModel):
    author = models.ForeignKey(UserProfile, related_name=u'message')
    chat = models.ForeignKey("chat.Chat", related_name=u'message')

class Chat(CreatableModel, UpdatableModel):
    author = models.ForeignKey(UserProfile, related_name=u'own_chat')
    users = models.ManyToManyField(UserProfile, related_name=u'chat')
