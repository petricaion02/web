from rest_framework import serializers
from user.models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):

    user = serializers.StringRelatedField()

    class Meta:
        model = UserProfile
        fields = ('id', 'user', 'gender', 'avatar')
