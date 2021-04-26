from django import forms

from base.utils import generate_bootstrap_widgets_for_all_fields

from . import (
    models
)


class Post(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = '__all__'
        widgets = generate_bootstrap_widgets_for_all_fields(models.Post)

