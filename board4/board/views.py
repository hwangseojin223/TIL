from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_safe, require_POST, require_http_methods

from .models import Article
from .forms import ArticleForm
# Create your views here.

@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'GET':
        form = ArticleForm()
    elif request.method == 'POST':
        form = ArticleForm(data=request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('board:detail', article.pk)
    return render(request, 'board/form.html', {
        'form': form,
    })
        
@require_safe
def index(request):
    articles = Article.objects.all()
    return render(request, 'board/index.html', {
        'articles': articles,
    })

@require_safe
def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'board/detail.html', {
        'article': article,
    })

@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'GET':
        form = ArticleForm(instance=article)
    elif request.method == 'POST':
        form = ArticleForm(data=request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect('board:detail', article.pk)
    return render(request, 'board/form.html',{
        'form':form,
    })

@require_POST
def delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    return redirect('board:index')