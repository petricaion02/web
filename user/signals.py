from django.contrib.auth.models import User
from django.db.models import F
from django.db.models.signals import post_save, post_delete

from user.models import UserProfile
from rest_framework.authtoken.models import Token


def user_post_save(sender, **kwargs):

    print("user post save", kwargs)
    if (kwargs.get('created', True)):
        UserProfile.objects.create(user=kwargs.get('instance'))
        Token.objects.create(user=instance)


post_save.connect(user_post_save, User)
