#! -*- encoding: UTF-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.db import IntegrityError

from base import utils


class UserProfile(models.Model):
    """
    Model for extended information of User at django.contrib.auth
    """

    # One to one references to User Model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Activation toke for email verification
    activation_token = models.CharField(max_length=40, blank=True)
    # Expiration date for activation token
    expiration = models.DateTimeField(blank=True, null=True)

    # Slug
    slug = models.SlugField(blank=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.slug:
            self.slug = slugify(self.user.username)
        successful_save = False
        saved_object = None
        while not successful_save:
            try:
                saved_object = super(UserProfile, self).save(force_insert, force_update, using, update_fields)
                successful_save = True
            except IntegrityError:
                self.slug = self.slug[:-4] + "-" + utils.generate_random_string(4)
        return saved_object

    def __str__(self):
        return str(self.user)
