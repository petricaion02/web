from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.fields import GenericRelation
from abstract.models import CreatableModel, UpdatableModel
from like.models import LikableModel
from event.models import MentionableModel


class CommentableModel(models.Model):

    comment = GenericRelation("comment.Comment", object_id_field="item_id",
                              content_type_field="item_type")
    comments_count = models.IntegerField(default=0)

    class Meta:
        abstract = True


class Comment(CreatableModel, UpdatableModel, LikableModel, MentionableModel,
              CommentableModel):

    user = models.ForeignKey("user.UserProfile", related_name="comment")
    item_type = models.ForeignKey(ContentType, related_name=u'comment')
    item_id = models.PositiveIntegerField()
    item = GenericForeignKey('item_type', 'item_id')
    text = models.TextField(default='')

    class Meta:
        verbose_name = u'Comment'
        verbose_name_plural = u'Comments'

    def get_involved_users(self):
        return set([self.user, self.item_type.model_class().objects.get(id=self.item_id).user])
