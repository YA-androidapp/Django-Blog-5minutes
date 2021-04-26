#! -*- coding: UTF-8 -*-
import importlib

from django.utils.translation import ugettext_lazy as _
from django.conf import LazySettings

settings = LazySettings()


def get_from_settings_or_default(var_name, default):
    try:
        return settings.__getattr__(var_name)
    except AttributeError:
        return default

# URL NAMES and other important module global variables


AUTH_NAMESPACE = get_from_settings_or_default('AUTH_NAMESPACE', "authentication")

LOGIN_URL = "log_in"
LOGOUT_URL = "log_out"
SIGNUP_URL = "sign_up"
SIGNUP_CONFIRM_URL = "sign_up_confirm"
CHANGE_PASSWORD_URL = "change_password"
CHANGE_PASSWORD_DONE_URL = "password_change_done"
RESET_PASSWORD_URL = "password_reset"
RESET_PASSWORD_DONE_URL = "password_reset_done"
RESET_PASSWORD_CONFIRM_URL = "password_reset_confirm"
RESET_PASSWORD_COMPLETE_URL = "password_reset_complete"

INVALID_URL = _('Invalid URL')
EXPIRED_URL = _('Expired URL')
PERMISSION_DENIED = _('You have not the proper permissions to enter this site')

# This configurations should be modified are loaded from settings

AUTH_UNIQUE_EMAIL = get_from_settings_or_default('AUTH_UNIQUE_EMAIL', False)
AUTH_VERIFY_EMAIL = get_from_settings_or_default('AUTH_VERIFY_EMAIL', False)

AUTH_ALLOW_SIGNUP = get_from_settings_or_default('AUTH_ALLOW_SIGNUP', False)
AUTH_ALLOW_PASSWORD_RECOVERY = get_from_settings_or_default('AUTH_ALLOW_PASSWORD_RECOVERY', False)

# Email Settings
AUTH_EMAIL_FROM = get_from_settings_or_default('AUTH_EMAIL_FROM', "")
AUTH_EMAIL_SUBJECT = get_from_settings_or_default('AUTH_EMAIL_SUBJECT', _("Confirmation email"))
AUTH_EMAIL_BODY = get_from_settings_or_default(
    'AUTH_EMAIL_BODY',
    _("Thanks for register, please, visit the next link to activate your account: ")
)

# Domain Settings
AUTH_DOMAIN = get_from_settings_or_default('AUTH_DOMAIN', "https://contraslash.com")

AUTH_PAGE_403 = get_from_settings_or_default('AUTH_PAGE_403', "403.html")

AUTH_USER_SIGNUP_FORM_MODULE = "applications.authentication.forms"

AUTH_USER_SIGNUP_FORM = getattr(
    importlib.import_module(
        AUTH_USER_SIGNUP_FORM_MODULE
    ),
    get_from_settings_or_default(
        'AUTH_USER_SIGNUP_FORM',
        "UserBaseForm"
    )
)


AUTH_INDEX_URL_NAME = get_from_settings_or_default('AUTH_INDEX_URL_NAME', "index")
AUTH_TEMPLATE_FOLDER = get_from_settings_or_default('AUTH_TEMPLATE_FOLDER', "authentication")
AUTH_REDIRECT_FIELD_NAME = get_from_settings_or_default('AUTH_TEMPLATE_FOLDER', "next")

# Messages Settings
AUTH_CONFIRM_ACCOUNT = get_from_settings_or_default(
    'AUTH_CONFIRM_ACCOUNT',
    _("Please confirm your account")
)
AUTH_ACCOUNT_CONFIRMATION_SUCCESSFUL = get_from_settings_or_default(
    'AUTH_ACCOUNT_CONFIRMATION_SUCCESSFUL',
    _("Your account has been activated")
)
AUTH_USER_CANT_BE_CREATED = get_from_settings_or_default(
    'AUTH_USER_CANT_BE_CREATED',
    _("User can't be created")
)

AUTH_DUPLICATED_EMAIL_ERROR_MESSAGE = get_from_settings_or_default(
    'AUTH_DUPLICATED_EMAIL_ERROR_MESSAGE',
    _("Duplicated email")
)

