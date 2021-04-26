from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        'authentication/',
        include(
            "applications.authentication.urls",
        )
    ),
    path(
        '',
        include(
            "applications.myblog.urls_slug",
        )
    ),
]
