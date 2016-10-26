from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^all/$', views.PostList.as_view(), name='all_posts'),
]
