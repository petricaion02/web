from rest_framework import viewsets
from like.models import Like
from like.serializer import LikeSerializer
from application.permissions import IsOwnerOrReadOnly
from rest_framework import permissions
from django.contrib.contenttypes.models import ContentType
from abstract.views import GenericRelationsModelViewSet
from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope

class LikeViewSet(GenericRelationsModelViewSet):
    serializer_class = LikeSerializer
    queryset = Like.objects.all()
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly,
                          TokenHasReadWriteScope)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user.profile)
