from http.client import HTTPResponse
from random import randint
from re import search
from tkinter import E
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Article, Post
from .forms import ArticleForm, PostForm
from django.contrib.postgres.search import SearchHeadline, SearchQuery

from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.urls import NoReverseMatch
from django.db.models import Count



import io
from django.http import FileResponse
from reportlab.pdfgen import canvas

def home(request):
    template_name = 'articles/articles.html'
    article = Article.objects.all()[:20]

    


    context = {
        'articles': article,

    }
    return render(request, template_name, context=context)


def create_post(request):
    template_name = 'posts/create_post.html'
    form = PostForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form = PostForm(request.POST or None)
            form.save()
            return redirect(home)
        else:
            return HttpResponse('Not submitted')
    context = {
        'form': form
    }
    return render(request, template_name, context=context)


def create_article(request):
    template_name = 'articles/create_article.html'
    form = ArticleForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form = ArticleForm(request.POST or None)
            form.save()
            return redirect(home)
        else:
            return HttpResponse('Not submitted')
    context = {
        'form': form
    }
    return render(request, template_name, context=context)

def view_post(request, id):
    try:
        template_name = 'posts/load_posts.html'
        post = Post.objects.get(id=id)
        post_article = post.article
        articles = Post.objects.filter(article=post_article)
        context = {
            'post': post,
            'articles': articles
        }
        return render(request, template_name, context=context)
    except NoReverseMatch:
        return redirect(home)
    except ObjectDoesNotExist:
        return redirect(home)





def update_post(request, id):
    template_name = 'posts/update_post.html'
    get_post = Post.objects.get(id=id)
    form = PostForm(request.POST or None, instance=get_post)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(view_post, id)
        else:
            return HttpResponse('Not submitted')
    context = {
        'form': form
    }
    return render(request, template_name, context=context)


def delete_post(request, id):
    template_name = 'posts/delete_post.html'
    messages.error(request, 'Document deleted.')
    get_post = Post.objects.get(id=id)
    get_post.delete()
    return render(request, template_name, context=None)


def all_post(request, id):

    template_name = 'posts/all_post.html'
    article = Article.objects.get(id=id)
    posts = article.post_set.all()

    context = {
        'article': article,
        'posts': posts,
    }

    return render(request, template_name, context=context)


def search_post(request):
    template_name = 'posts/search_post.html'
    result_html = 'posts/results.html'
    results = ''
    if request.method == 'POST':
        query = request.POST.get('search', '1')
        searched_query = SearchQuery(query)

        search_headline = SearchHeadline("content", searched_query,
        start_sel='<span class="font-bold text-red-400 text-3xl">',
            stop_sel='</span>')

        results = Post.objects.annotate(
            headline=search_headline,
       
        ).filter(content__search=searched_query)[:10]
        article = Post.objects.annotate(
            headline=search_headline,
       
        ).filter(title__search=searched_query)[:10]
        context = {
        'results': results,
        'articles': article
        }
        return render(request,result_html, context=context)
    else:
        context = {
            'result': '1'
        }
        return render(request, template_name, context=context)


    



def export_to_pdf(request, id):

    post = Post.objects.get(id=id)
    content = post.content
    try:
        f = open(f"exported/exported-{post.id}.md", "w")
        f.write(content)
        f.close()
    except FileExistsError:
        f = open(f"exported/exported-{post.id}.md", "w")
        f.write(content)
        f.close()

    return redirect(home)

def posts(request):
    template_name = 'posts/posts.html'
    posts = Post.objects.all()[:10]
    context = {
        'posts': posts
    }
    return render(request, template_name, context=context)