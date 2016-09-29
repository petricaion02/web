from django.db import models

# Create your models here.

from abstract.models import CreatableModel, UpdatableModel
from like.models import LikableModel
from comment.models import CommentableModel
from user.models import UserProfile
from image.models import Image

class Post(CreatableModel, UpdatableModel, LikableModel, CommentableModel):
    author = models.ForeignKey(UserProfile, related_name=u'post')
    text = models.TextField(default='')
    attachments = models.ManyToManyField(Image, related_name=u'post')
