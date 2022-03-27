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
            'class': 'focus:ring-0  placeholder-yellow-100 border-yellow-300 border-2 focus:border-yellow-300 bg-transparent focus:outline-none',
            'placeholder': 'Title',
            }),

            'content': forms.Textarea(attrs={
            'class': 'resize w-11/12  h-full placeholder-yellow-100  focus:border-yellow-300 bg-transparent focus:outline-none',
            'cols': '150',
          
            'placeholder': 'content',
            }),
        }



class ArticleForm(ModelForm):


    class Meta:
        model = models.Article
        fields = ('title', 'content' )
        widgets = {
            'title': forms.TextInput(attrs={
            'class': 'focus:ring-0  placeholder-yellow-100 border-yellow-300 border-2 focus:border-yellow-300 bg-transparent focus:outline-none',
            'placeholder': 'Title',
            }),

            'content': forms.Textarea(attrs={
            'class': 'resize w-11/12  h-full placeholder-yellow-100  focus:border-yellow-300 bg-transparent focus:outline-none',
            'cols': '150',
          
            'placeholder': 'content',
            }),
        }