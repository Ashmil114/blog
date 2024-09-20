from django import forms
from .models import tb_post, tb_category


class category_form(forms.ModelForm):
    class Meta:
        model = tb_category
        fields = ["title"]


class post_form(forms.ModelForm):

    class Meta:
        model = tb_post
        fields = ["title", "image", "description", "category"]
