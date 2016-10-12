from django.shortcuts import render
from rest_framework import generics
from user.serializer import UserProfileSerializer
from user.models import UserProfile
# Create your views here.

from rest_framework import viewsets


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
