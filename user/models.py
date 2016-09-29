from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from image.models import Image
from abstract.models import CreatableModel, UpdatableModel

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('P', 'Prefer not to answer'),
)

class UserProfile(CreatableModel, UpdatableModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                related_name='profile',
                                verbose_name=u'User')

    gender = models.CharField(max_length=1,
                              choices=GENDER_CHOICES, default='P')

    avatar = models.ForeignKey(Image, verbose_name=u'Avatar', null=True,
                               blank=True)

    class Meta:
        verbose_name = u'User profile'
        verbose_name_plural = u'User profiles'

    def __str__(self):
       return self.user.username

# Create your models here.
