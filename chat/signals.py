from django.db.models.signals import post_save
from chat.models import Chat


def chat_post_save(sender, **kwargs):

    chat = kwargs.get('instance')

    if (not chat.title):
        users = sender.objects.get(pk=chat.pk).users
        chat.title = "Unnamed" + ' '.join(map(str, users.all())) #AARGH
        chat.save()

post_save.connect(chat_post_save, Chat)
