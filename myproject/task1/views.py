from django.http import HttpResponse
from .forms import UseForm
from django.shortcuts import render
from django.views.generic import TemplateView
from task1.models import Game, Buyer

# Create your views here.
def index(request):
    return render(request, 'second_task/index.html')


class index2(TemplateView):
    template_name = 'second_task/index2.html'


class platform(TemplateView):
    template_name = 'fourth_task/platform.html'


class games(TemplateView):
    template_name = 'fourth_task/games.html'

    games = Game.objects.all()

    games_temp = []
    for game_i in games:
        descript_lst = [game_i.title, game_i.description, float(game_i.cost)]
        games_temp.append(descript_lst)

    extra_context = {
        'games': games_temp
    }


class cart(TemplateView):
    template_name = 'fourth_task/cart.html'


def sign_up_by_html(request):
    context = {}
    is_by_django = False
    context['is_by_django'] = is_by_django
    users = ['Andrey', 'Den', 'Serg']
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(request.POST.get('age'))

        if (password == repeat_password) and (age >= 18) and (username not in users):
            welcome = f'Приветствуем, {username}!'
            context['welcome'] = welcome
            return render(request, 'fifth_task/registration_page.html', context)
        elif password != repeat_password:
            info['error'] = 'Пароли не совпадают'
            context['info'] = info
            return render(request, 'fifth_task/registration_page.html', context)
        elif age < 18:
            info['error'] = 'Вы должны быть старше 18'
            context['info'] = info
            return render(request, 'fifth_task/registration_page.html', context)
        elif username in users:
            info['error'] = 'Пользователь уже существует'
            context['info'] = info
            return render(request, 'fifth_task/registration_page.html', context)

    return render(request, 'fifth_task/registration_page.html', context)


def sign_up_by_django(request):
    context = {}
    is_by_django = True
    context['is_by_django'] = is_by_django

    if request.method == 'POST':
        info = {}
        form = UseForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username_dj']
            password = form.cleaned_data['password_dj']
            repeat_password = form.cleaned_data['repeat_password_dj']
            age = int(form.cleaned_data['age_dj'])
        else:
            info['error'] = 'Некорректные данные'
            context['info'] = info
            return render(request, 'fifth_task/registration_page.html', context)

        username_in_users = Buyer.objects.filter(name=username).first()

        if (password == repeat_password) and (age >= 18) and (username_in_users is None):
            welcome = f'Приветствуем, {username}!'
            context['welcome'] = welcome
            Buyer.objects.create(name=username, balance=100.0, age=age)
            return render(request, 'fifth_task/registration_page.html', context)
        elif password != repeat_password:
            info['error'] = 'Пароли не совпадают'
            context['info'] = info
            return render(request, 'fifth_task/registration_page.html', context)
        elif age < 18:
            info['error'] = 'Вы должны быть старше 18'
            context['info'] = info
            return render(request, 'fifth_task/registration_page.html', context)
        elif not username_in_users is None:
            info['error'] = 'Пользователь уже существует'
            context['info'] = info
            return render(request, 'fifth_task/registration_page.html', context)
    else:
        form = UseForm(request.POST)

    context['form'] = form
    return render(request, 'fifth_task/registration_page.html', context)
