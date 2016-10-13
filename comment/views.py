from rest_framework import viewsets
from comment.models import Comment
from comment.serializer import CommentSerializer
from application.permissions import IsOwnerOrReadOnly
from rest_framework import permissions
from django.contrib.contenttypes.models import ContentType
from abstract.views import GenericRelationsModelViewSet
from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope

class CommentViewSet(GenericRelationsModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly,
                          TokenHasReadWriteScope)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user.profile)
