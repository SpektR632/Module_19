from django.shortcuts import render
from .forms import UserRegister
from .models import Buyer, Game


# Create your views here.
def home(request):
    context = {
        'home_text': 'Главная страница',
        'home_page': 'Главная',
        'shop': 'Магазин',
        'cart': 'Корзина'
    }
    return render(request, 'Home.html', context)


def shop(request):
    context = {
        'shop_text': "Игры",
        'games': Game.objects.all(),
        'buy': 'Купить',
        'back': 'Вернуться обратно'
    }
    return render(request, 'shop.html', context)


def cart(request):
    context = {
        'cart': 'Корзина',
        'cart_text': "Корзина пуста, добавьте уже что-то!",
        'back': 'Вернуться обратно'
    }
    return render(request, 'basket.html', context)


def sign_up_by_django(request):
    users = Buyer.objects.all()
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if password == repeat_password and int(age) >= 18 and username not in [i.name for i in users]:
                Buyer.objects.create(name=username, age=age)
            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif int(age) < 18:
                info['error'] = 'Вы должны быть старше 18'
            else:
                info['error'] = 'Пользователь уже существует'
    else:
        form = UserRegister()
    return render(request, 'registration_page.html', context=info)