from django.conf.urls import url, include
from rest_framework import routers

from user.views import UserProfileViewSet
from post.views import PostViewSet
from image.views import ImageViewSet
from comment.views import CommentViewSet
from like.views import LikeViewSet
from chat.views import ChatViewSet, MessageViewSet

from rest_framework import authtoken
router = routers.DefaultRouter()
router.register(r'user', UserProfileViewSet, base_name='user')
router.register(r'post', PostViewSet, base_name='post')
router.register(r'image', ImageViewSet, base_name='image')
router.register(r'comment', CommentViewSet, base_name='comment')
router.register(r'like', LikeViewSet, base_name='like')
router.register(r'chat', ChatViewSet, base_name='chat')
router.register(r'message', MessageViewSet, base_name='message')

urlpatterns = router.urls

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', authtoken.views.obtain_auth_token),
]
