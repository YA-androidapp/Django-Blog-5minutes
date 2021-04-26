#! -*- encoding: UTF-8 -*-
from django.contrib.auth.mixins import LoginRequiredMixin, AccessMixin, PermissionRequiredMixin
from django.contrib import messages
from django import http
try:
    from django.core.urlresolvers import reverse_lazy
except ImportError:
    from django.urls import reverse_lazy
from django.template.loader import get_template
from django import http

from . import conf


class CustomLoginRequiredMixin(LoginRequiredMixin):
    """
    Generic Mixin to make an user to be authenticated before see system information
    """
    login_url = conf.LOGIN_URL


class CustomPermissionRequiredMixin(PermissionRequiredMixin):

    def handle_no_permission(self):
        return http.HttpResponseForbidden(get_template(conf.AUTH_PAGE_403).render())


class AlreadyAuthenticatedMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return http.HttpResponseRedirect(
                reverse_lazy(conf.AUTH_INDEX_URL_NAME)
            )
        else:
            return super(AlreadyAuthenticatedMixin, self).dispatch(request, *args, **kwargs)


class SuperAdminRequiredMixin(AccessMixin):
    """
    Generic mixin to ensure user logged is super_user
    CBV mixin which verifies that the current user is authenticated.
    """
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        else:
            if request.user.is_staff:
                return super(SuperAdminRequiredMixin, self).dispatch(request, *args, **kwargs)
            else:
                messages.add_message(
                    request,
                    messages.ERROR,
                    conf.PERMISSION_DENIED
                )
                return self.handle_no_permission()
