from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^chats/$', views.chats, name='chats'),
    url(r'^chat/(?P<pk>\d+)/$', views.chat, name='chat'),
]
