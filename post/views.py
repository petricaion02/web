from rest_framework import viewsets
from post.models import Post
from user.models import FriendShip
from post.serializer import PostSerializer
from application.permissions import IsOwnerOrReadOnly
from rest_framework import permissions
from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.db.models import Q


#TODO: Fix permissions

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly,
                          TokenHasReadWriteScope)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user.profile)

    def get_queryset(self):
        qs = super().get_queryset()
        user_friends_qs = \
            FriendShip.objects.filter(first_user=self.request.user.profile)

        qs = qs \
            .filter(Q(user__user=self.request.user) |
                    Q(user__me_requests__in=user_friends_qs))
        if self.request.query_params.get('username'):
            qs = qs.filter(user__user__username=
                self.request.query_params.get('username'))
        if self.request.query_params.get('q'):
            qs = qs.filter(
                Q(text__icontains=self.request.query_params.get('q')) |
                Q(title__icontains=self.request.query_params.get('q'))
            )
        return qs

class PostList(ListView):
    model = Post
    template_name = "post/post_list.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ListView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        user_friends_qs = \
            FriendShip.objects.filter(first_user=self.request.user.profile)

        queryset = Post.objects \
            .filter(Q(user__user=self.request.user) |
                    Q(user__me_requests__in=user_friends_qs))
        return queryset
