from django.db import models

# Create your models here.

from abstract.models import CreatableModel, UpdatableModel
from like.models import LikableModel
from comment.models import CommentableModel
from user.models import UserProfile
from image.models import Image
from event.models import MentionableModel


class Post(CreatableModel, UpdatableModel, LikableModel, CommentableModel,
           MentionableModel):

    user = models.ForeignKey("user.UserProfile", related_name="post")
    title = models.TextField(default='')
    text = models.TextField(default='')
    attachments = models.ManyToManyField(Image, related_name=u'post', blank=True)

    def get_involved_users(self):
        return set([self.user])
