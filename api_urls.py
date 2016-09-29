from django.conf.urls import url, include
from rest_framework import routers

from user.views import UserProfileViewSet
from rest_framework import authtoken
router = routers.DefaultRouter()
router.register(r'user', UserProfileViewSet, base_name='user')

urlpatterns = router.urls

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', authtoken.views.obtain_auth_token),
]
