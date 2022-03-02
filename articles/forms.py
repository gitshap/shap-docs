from django.forms import ModelForm
from django import forms
from articles import models
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, ButtonHolder, Submit



class PostForm(ModelForm):


    class Meta:
        model = models.Post
        fields = ('title', 'content', 'article', )
        widgets = {
            'title': forms.TextInput(attrs={
            'class': 'bg-red-100',
            'placeholder': 'Title',
            }),

            'content': forms.Textarea(attrs={
            'class': 'resize w-10/12',
            'cols': '250',
            'placeholder': 'content',
            }),
        }


