from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.contenttypes.models import ContentType
from application.permissions import IsOwnerOrReadOnly
from rest_framework import permissions
# Create your views here.


class GenericRelationsModelViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)

    def get_queryset(self):
        qs = super().get_queryset()
        item_model = self.request.query_params.get('item_type')
        item_id = self.request.query_params.get('item_id')

        if item_model:
            item_type = ContentType.objects.get(model=item_model)
            if item_model:
                qs = qs.filter(item_type=item_type)
        if item_id:
            qs = qs.filter(item_id=item_id)
        return qs
