from django.db import models
from django.contrib.auth import models as auth_models

from base import models as base_models

from . import (
    conf
)


class Post(base_models.FullSlugBaseModel):
    class Meta:
        app_label = 'myblog'

    author = models.ForeignKey(auth_models.User, on_delete=models.CASCADE)
    url_name = conf.POST_DETAIL_URL_NAME
