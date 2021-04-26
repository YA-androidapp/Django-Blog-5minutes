#! -*- coding: UTF-8 -*-

from django.http import  HttpResponseForbidden
from django.template.loader import get_template
from django.core.urlresolvers import reverse_lazy


from . import models as authentication_models


def check_permissions(function):
    """
    Decorator for verify access control in default URL, based on custom permission defined in Permission model.
    Using check_permissions decorator, the system will verify the access to an user to respective view.

    Recomended for use in dispatch method in Django Class Based Views
    :param function: Function to wrap
    :return: Function to continue or HttpForbidden action
    """
    def inner_check(*args, **kwargs):
        request = None
        if kwargs.get('request', False):
            request = kwargs['request']
        else:
            for arg in args:
                if 'request' in arg.__class__.__name__.lower():
                    request = arg
        if request is not None:
            profile = authentication_models.UserProfile.objects.get(user=request.user)
            role = profile.role
            request_name = request.resolver_match.url_name
            permissions = authentication_models.Permission.objects.filter(role=role, reverse_lazy_url=request_name)

            if not permissions:
                return HttpResponseForbidden(get_template('403.html').render({}))

        return function(*args, **kwargs)
    return inner_check
