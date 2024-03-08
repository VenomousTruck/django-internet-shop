from django.shortcuts import render
from django.http import HttpResponse
from goods.models import Categories


def index(request):
    categories = Categories.objects.all()

    context = {
        'title': 'Home - Главная',
        'content': 'Магазин мебели HOME',
        'categories': categories,
    }
    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'Home - О компании',
        'content': 'О нас',
        'text_on_page': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Assumenda dolores earum molestiae quod voluptatibus. Deleniti dolorem, fugit illum laborum magnam magni maiores minima provident qui reprehenderit suscipit temporibus tenetur voluptatibus!'
    }

    return render(request, 'main/about.html', context)


