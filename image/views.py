from rest_framework import viewsets
from image.models import Image
from image.serializer import ImageSerializer
from application.permissions import IsOwnerOrReadOnly
from rest_framework import permissions
from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope

class ImageViewSet(viewsets.ModelViewSet):
    serializer_class = ImageSerializer
    queryset = Image.objects.all()
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly,
                          TokenHasReadWriteScope)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user.profile)

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.query_params.get('username'):
            qs = qs.filter(user__user__username=self.request.query_params.get('username'))
        return qs
