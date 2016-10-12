from django.db.models import F
from django.db.models.signals import post_save, post_delete
from django.contrib.contenttypes.models import ContentType

from like.models import Like, LikableModel


def like_post_save(sender, **kwargs):

    if (kwargs.get('created', True)):
        like = kwargs.get('instance')
        print(like.item_type, like.item_id)
        item = like.item_type.model_class().objects.get(id=like.item_id)
        print(item)
        item.likes_count = F('likes_count') + 1
        item.save()


def like_post_delete(sender, **kwargs):

    like = kwargs.get('instance')
    item = like.item_type.model_class().objects.get(id=like.item_id)
    item.likes_count = F('likes_count') - 1
    item.save()


post_save.connect(like_post_save, Like)
post_delete.connect(like_post_delete, Like)
