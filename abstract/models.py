from django.db import models

# Create your models here.
class CreatableModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name=u'Create time')
    class Meta:
        abstract = True

class UpdatableModel(models.Model):
    updated_at = models.DateTimeField(auto_now=True,
                                      verbose_name=u'Create time')
    class Meta:
        abstract = True
