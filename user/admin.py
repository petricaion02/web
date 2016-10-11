from django.contrib import admin

from user.models import UserProfile, FriendShip


admin.site.register(UserProfile)
admin.site.register(FriendShip)

# Register your models here.
