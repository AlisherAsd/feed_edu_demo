from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login, logout
from django.urls import reverse
from django.views import View

from users.forms import UserRegistrationForm, LoginForm
from users.models import Role
from users.utils import get_data



menu = [
    {'title': 'Запросить', 'url': 'test_constructor'},
    {'title': 'Исходящие запросы', 'url': 'my_tests'},
    {'title': 'Личная страница', 'url': 'user_dashboard'},
    {'title': 'Входящие запросы', 'url': 'available_tests'},
    {'title': 'Пользователи', 'url': 'users'},
]



class user_dashboard(View):
    def get(self, request):
        user = request.user
        role =  Role.objects.get(id=user.role_id)
        data = {
            'title': 'Личная страница',
            'menu': menu,
            'user': user,
            'role': role,
        }
        return render(request, 'users/user_dashboard.html', context=data)


class users(View):
    def get(self, request):
        User = get_user_model()
        users = User.objects.all()
        roles = Role.objects.all()
        data = {
            'title': 'Список пользователей',
            'menu': menu,
            'users': users,
            'roles': roles,
        }
        return render(request, 'users/users.html', context=data)

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    auth_login(request, user)
                    return HttpResponseRedirect(reverse('user_dashboard'))
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Юзер не найден ')
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST, request.FILES)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'users/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'users/register.html', {'user_form': user_form})

@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))