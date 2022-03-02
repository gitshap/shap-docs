from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Article, Post
from .forms import PostForm



def home(request):
    template_name = 'articles/articles.html'
    article = Article.objects.all()


    get_network = Article.objects.get(title='Networks')
    networks = Post.objects.filter(article=get_network)
    context = {
        'article': article,

        'networks': networks
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


def view_post(request, id):
    template_name = 'posts/load_posts.html'
    post = Post.objects.get(id=id)

    context = {
        'post': post
    }
    return render(request, template_name, context=context)



def update_post(request, id):
    template_name = 'posts/update_post.html'
    get_post = Post.objects.get(id=id)
    form = PostForm(request.POST or None, instance=get_post)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(home)
        else:
            return HttpResponse('Not submitted')
    context = {
        'form': form
    }
    return render(request, template_name, context=context)