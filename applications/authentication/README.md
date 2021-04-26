# Authentication

Authentication is a simple django module that provides a simple wrapper for django.contrib.auth.views, 
adding a custom look and feel and a modified sign up method with email confirmation.

## Basic configuration
Add `applications.authentication` to your `INSTALLED_APPS` variable in
`settings.py`

To enable django authentication behavior with [django.contrib.auth.mixins.LoginRequired](https://docs.djangoproject.com/en/2.1/topics/auth/default/#the-loginrequired-mixin) use this line on yout `settings.py`

```python
if 'applications.authentication' in INSTALLED_APPS:
    LOGIN_URL = "log_in"
```

Also include the following in your `urls.py`

```python
path('', include("applications.authentication.urls"))
```

### Other common options

```python
AUTH_UNIQUE_EMAIL = False  # All emails must be uniques
AUTH_VERIFY_EMAIL = False  # Send a message to confirm email exists, SMTP configuration must be enabled

AUTH_ALLOW_SIGNUP = True  # Users can register by themselves
AUTH_ALLOW_PASSWORD_RECOVERY = True  # Provide methods to recover password, SMPT configuration must be enabled

AUTH_EMAIL_FROM = ""  # Email name show on message
AUTH_EMAIL_SUBJECT = "..."  # Email title for email confirmation
AUTH_EMAIL_BODY = "..."  # Email body for email confirmation

AUTH_INDEX_URL_NAME = "index"  # Default page to redirect after login
```

To modify templating, use in your `settings.py` the variable

```python
AUTH_TEMPLATE_FOLDER = "your_template_folder"
```


## Email configuration
To get this work, make sure you got the email configuration in you settings.py

An example for use Gmail SMTPs server:
```
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'myname@gmail.com'
EMAIL_HOST_PASSWORD = 'mypassword'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'nmyname@gmail.com'
```  

Also please edit the conf.py file, to customize your domain and other options

## Multilingual mode
If you change the Strings Settings, remember to recompile the locales

```
./manage.py compilemessages
```

And edit the locale folder, for more information visit [our blog](http://blog.contraslash.com/creando-locales-con-django/).

## Context processors

To enable LOGIN URLS in all templates add `applications.authentication.context_processors.authentication_urls`
to your context_processor,


## Contributing

This software is licensed under [MIT LICENCE](LICENSE), feel free to create
a Pull Request.

Enjoy and feel free to put an issue or write me to ma0@contraslash.com