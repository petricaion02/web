from django.db import models
from abstract.models import CreatableModel, UpdatableModel
from like.models import LikableModel
from comment.models import CommentableModel
# Create your models here.

class Image(CreatableModel, UpdatableModel, LikableModel, CommentableModel):
    file = models.ImageField(verbose_name='File')

    def __str__(self):
        return self.file.name
