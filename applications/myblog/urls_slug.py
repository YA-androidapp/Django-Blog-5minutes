from django.urls import path

from . import conf

urlpatterns = [

]

from .views import post

urlpatterns += [
    # post
    path(
        'post/',
        post.List.as_view(),
        name=conf.POST_LIST_URL_NAME
    ),
    path(
        'post/create/',
        post.Create.as_view(),
        name=conf.POST_CREATE_URL_NAME
    ),
    path(
        'post/<slug:slug>/',
        post.Detail.as_view(),
        name=conf.POST_DETAIL_URL_NAME
    ),
    path(
        'post/<slug:slug>/update/',
        post.Update.as_view(),
        name=conf.POST_UPDATE_URL_NAME
    ),
    path(
        'post/<slug:slug>/delete/',
        post.Delete.as_view(),
        name=conf.POST_DELETE_URL_NAME
    ),
]

