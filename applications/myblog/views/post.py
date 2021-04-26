from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
try:
    from django.core.urlresolvers import reverse_lazy
except ImportError:
    from django.urls import reverse_lazy
from django import http


from base import views as base_views

from .. import (
    models,
    forms,
    conf
)


class List(LoginRequiredMixin, base_views.BaseListView):
    """
    List all Posts
    """
    queryset = models.Post.objects.all()

    def __init__(self):
        super(List, self).__init__()

    def get_context_data(self, **kwargs):
        context = super(List, self).get_context_data(**kwargs)

        context['detail_url_name'] = conf.POST_DETAIL_URL_NAME

        if self.request.user.has_perm("myblog.add_post"):
            context['create_object_reversed_url'] = reverse_lazy(
                conf.POST_CREATE_URL_NAME
            )
        
        return context


class Create(LoginRequiredMixin, PermissionRequiredMixin, base_views.BaseCreateView):
    """
    Create a Post
    """
    model = models.Post
    permission_required = (
        'myblog.add_post'
    )
    form_class = forms.Post

    def __init__(self):
        super(Create, self).__init__()

    def get_success_url(self):
        return reverse_lazy(conf.POST_DETAIL_URL_NAME, kwargs=self.kwargs_for_reverse_url())


class Detail(LoginRequiredMixin, base_views.BaseDetailView):
    """
    Detail of a Post
    """
    model = models.Post

    def __init__(self):
        super(Detail, self).__init__()

    def get_context_data(self, **kwargs):
        context = super(Detail, self).get_context_data(**kwargs)

        if self.request.user.has_perm("myblog.change_post"):
            context['update_object_reversed_url'] = reverse_lazy(
                conf.POST_UPDATE_URL_NAME,
                kwargs=self.kwargs_for_reverse_url()
            )

        if self.request.user.has_perm("myblog.delete_post"):
            context['delete_object_reversed_url'] = reverse_lazy(
                conf.POST_DELETE_URL_NAME,
                kwargs=self.kwargs_for_reverse_url()
            )

        return context


class Update(LoginRequiredMixin, PermissionRequiredMixin, base_views.BaseUpdateView):
    """
    Update a Post
    """
    model = models.Post
    form_class = forms.Post
    permission_required = (
        'myblog.change_post'
    )

    def __init__(self):
        super(Update, self).__init__()

    def get_success_url(self):
        return reverse_lazy(conf.POST_DETAIL_URL_NAME, kwargs=self.kwargs_for_reverse_url())


class Delete(LoginRequiredMixin, PermissionRequiredMixin, base_views.BaseDeleteView):
    """
    Delete a Post
    """
    model = models.Post
    permission_required = (
        'myblog.delete_post'
    )

    def __init__(self):
        super(Delete, self).__init__()

    def get_success_url(self):
        return reverse_lazy(conf.POST_LIST_URL_NAME)
