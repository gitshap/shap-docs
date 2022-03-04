from http.client import HTTPResponse
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Article, Post
from .forms import PostForm


def home(request):
    template_name = 'articles/articles.html'
    article = Article.objects.all()

    get_network = Article.objects.get(title='Networks')
    networks = Post.objects.filter(article=get_network)

    get_licenses = Article.objects.get(title='Licenses')
    licenses = Post.objects.filter(article=get_licenses)

    get_server_2019 = Article.objects.get(title='Windows Server 2019')
    server_2019 = Post.objects.filter(article=get_server_2019)

    get_processes = Article.objects.get(title='Internal IT Processes')
    processes = Post.objects.filter(article=get_processes)

    get_google = Article.objects.get(title='Google Workspace')
    google = Post.objects.filter(article=get_google)

    get_workstations = Article.objects.get(title='Workstations')
    workstation = Post.objects.filter(article=get_workstations)

    get_nas = Article.objects.get(title='NAS')
    nas = Post.objects.filter(article=get_nas)

    get_tools = Article.objects.get(title='Internal Tools')
    tools = Post.objects.filter(article=get_tools)

    context = {
        'article': article,

        'networks': networks,
        'licenses': licenses,
        'server_2019': server_2019,
        'processes': processes,
        'google': google,
        'workstation': workstation,
        'nas': nas,
        'tools': tools

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
    post_article = post.article
    articles = Post.objects.filter(article=post_article)

    context = {
        'post': post,
        'articles': articles
    }
    return render(request, template_name, context=context)


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
    get_post = Post.objects.get(id=id)
    get_post.delete()
    return redirect(home)


def all_post(request, id):

    template_name = 'posts/all_post.html'
    article = Article.objects.get(id=id)
    get_network = Article.objects.get(title='Networks')
    networks = Post.objects.filter(article=get_network)

    get_licenses = Article.objects.get(title='Licenses')
    licenses = Post.objects.filter(article=get_licenses)

    get_server_2019 = Article.objects.get(title='Windows Server 2019')
    server_2019 = Post.objects.filter(article=get_server_2019)

    get_processes = Article.objects.get(title='Internal IT Processes')
    processes = Post.objects.filter(article=get_processes)

    get_google = Article.objects.get(title='Google Workspace')
    google = Post.objects.filter(article=get_google)

    get_workstations = Article.objects.get(title='Workstations')
    workstation = Post.objects.filter(article=get_workstations)

    get_nas = Article.objects.get(title='NAS')
    nas = Post.objects.filter(article=get_nas)

    get_tools = Article.objects.get(title='Internal Tools')
    tools = Post.objects.filter(article=get_tools)

    context = {
        'article': article,

        'networks': networks,
        'licenses': licenses,
        'server_2019': server_2019,
        'processes': processes,
        'google': google,
        'workstation': workstation,
        'nas': nas,
        'tools': tools

    }

    return render(request, template_name, context=context)


def search_post(request):
    template_name = 'posts/search_post.html'
    result_html = 'posts/results.html'
    results = ''
    if request.method == 'POST':
        query = request.POST.get('search', '1')
        results = Post.objects.filter(content__icontains=query)
        article = Post.objects.filter(title__icontains=query)
        print(results)
        context = {
        'results': results,
        'article': article
        }
        return render(request,result_html, context=context)
    else:
        context = {
            'result': '1'
        }
        return render(request, template_name, context=context)


    

    