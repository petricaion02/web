from django.db.models import F
from django.db.models.signals import post_save, post_delete
from django.contrib.contenttypes.models import ContentType

from comment.models import Comment


def comment_post_save(sender, **kwargs):
    print(kwargs)

    if (kwargs.get('created', True)):
        comment = kwargs.get('instance')
        item = comment.item_type.model_class().objects.get(id=comment.item_id)
        item.comments_count = F('comments_count') + 1
        item.save()


def comment_post_delete(sender, **kwargs):
    comment = kwargs.get('instance')
    item = comment.item_type.model_class().objects.get(id=comment.item_id)
    item.comments_count = F('comments_count') - 1
    item.save()


post_save.connect(comment_post_save, Comment)
post_delete.connect(comment_post_delete, Comment)
