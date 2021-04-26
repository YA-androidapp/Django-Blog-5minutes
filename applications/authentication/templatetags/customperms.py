from django import template

from .. import models as authentication_models

register = template.Library()


@register.filter(name='check_perms')
def check_perms(user, reverse_url):
    """
    Template tag for verify the access of an user to a view
    :param user: User from django.contrib.auth
    :param reverse_url: Url Name to verify
    :return: List of permission, if is empty, the user has not permission
    """
    role = authentication_models.UserProfile.objects.get(user=user).role
    return authentication_models.Permission.objects.filter(role=role, reverse_lazy_url=reverse_url)


@register.filter(name='get_role')
def get_role(user):
    """
    Return the role of the current authenticated user
    :param user: User form django.contrib.auth
    :return: Role in the system
    """
    return authentication_models.UserProfile.objects.get(user=user).role.short_name