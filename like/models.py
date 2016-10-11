from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.fields import GenericRelation
from abstract.models import CreatableModel
from event.models import MentionableModel


class Like(CreatableModel, MentionableModel):

    user = models.ForeignKey('user.UserProfile', related_name=u'like',
                             verbose_name=u'User')
    item_type = models.ForeignKey(ContentType, related_name=u'like')
    item_id = models.PositiveIntegerField()
    item = GenericForeignKey('item_type', 'item_id')

    class Meta:
        verbose_name = u'Like'
        verbose_name_plural = u'Likes'
        unique_together = ["user", "item_type", "item_id"]

    def get_involved_users(self):
        return set([self.item_type.model_class().objects.get(id=self.item_id).user, self.user])

    def __str__(self):
        return str(self.user) + ' like to ' \
               + str(self.item_type) + ' #' \
               + str(self.item_id)


class LikableModel(models.Model):

    likes = GenericRelation(Like, object_id_field="item_id",
                              content_type_field="item_type")
    likes_count = models.IntegerField(default=0)

    class Meta:
        abstract = True
