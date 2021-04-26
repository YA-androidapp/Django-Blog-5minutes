try:
    from django.core.urlresolvers import reverse_lazy
except ImportError:
    from django.urls import reverse_lazy

from . import conf


def authentication_urls(request):
    return {
        "log_in_url": reverse_lazy(conf.LOGIN_URL),
        "log_out_url": reverse_lazy(conf.LOGOUT_URL),
        "sign_up_url": reverse_lazy(conf.SIGNUP_URL),
        "password_reset_url": reverse_lazy(conf.RESET_PASSWORD_URL)
    }
