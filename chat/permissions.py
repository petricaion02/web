from rest_framework import permissions

class IsInChatMessage(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(obj.chat.users.all()
                        .filter(pk=request.user.profile.pk).count())


class IsInChat(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(obj.users.all()
                        .filter(pk=request.user.profile.pk).count())
