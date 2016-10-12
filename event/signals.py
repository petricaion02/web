from django.db.models import F
from django.db.models.signals import post_save, post_delete
from django.contrib.contenttypes.models import ContentType

from event.models import Event, MentionableModel


def mentionable_post_save(sender, **kwargs):
    item = kwargs.get('instance')

    if (kwargs.get('created', True)):
        event = Event(type='C',
                      item=item)
        event.save()
        for user in item.get_involved_users():
            event.users.add(user)
    else:
        event = Event(type='U',
                      item=item)
        event.save()
        for user in item.get_involved_users():
            event.users.add(user)


for model in MentionableModel.__subclasses__():
    post_save.connect(mentionable_post_save, model)
