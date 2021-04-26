from django.contrib import admin
from django.contrib.auth.models import  Permission
from django.contrib.contenttypes.models import ContentType

from . import models as authentication_models
# Register your models here.
admin.site.register(authentication_models.UserProfile)
admin.site.register(Permission)
admin.site.register(ContentType)

