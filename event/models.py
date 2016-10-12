from django.db import models

from abstract.models import CreatableModel
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.fields import GenericRelation
# Create your models here.

EVENT_TYPE_CHOICES = (
    ('C', 'Create'),
    ('U', 'Update'),
)


class Event(CreatableModel):

    users = models.ManyToManyField('user.UserProfile', related_name='event')
    action_type = models.CharField(max_length=1, choices=EVENT_TYPE_CHOICES)
    item_type = models.ForeignKey(ContentType, related_name=u'event')
    item_id = models.PositiveIntegerField()
    item = GenericForeignKey('item_type', 'item_id')

    class Meta:
        verbose_name = u'Event'
        verbose_name_plural = u'Events'

    def __str__(self):
        return str(self.type) + "'s' event"


class MentionableModel(models.Model):

    events = GenericRelation(Event, object_id_field="item_id",
                             content_type_field="item_type")

    def getInvolvedUsers(self):
        pass

    class Meta:
        abstract = True
