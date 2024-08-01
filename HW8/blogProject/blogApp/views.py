from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Category

# Create your views here.
def new(request):
    if request.method == 'POST':
        category = get_object_or_404(Category, id=request.POST['category'])
        new_article = Article.objects.create(
            title=request.POST['title'],
            content=request.POST['content'],
            category=category
        )
        return redirect('list')

    categories = Category.objects.all()
    return render(request, 'new.html', {'categories': categories})

def list(request):
    articles = Article.objects.all()
    categories = Category.objects.all()
    return render(request, 'list.html', {'articles': articles, 'categories': categories})


def category_posts(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    articles = category.articles.all()
    return render(request, 'category.html', {'category': category, 'articles': articles})

def detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'detail.html', {'article': article})
