from django.views.generic import CreateView
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.db import connection

class SignupView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'



def public_home(request):
    db_engine = connection.settings_dict['ENGINE'].split('.')[-1]
    db_name = connection.settings_dict['NAME']
    db_info = f"PostgreSQL: {db_name}"
    
    return render(request, 'home.html', {
        'message': f'Войдите! БД: {db_info}',
        'db_engine': db_engine
    })

@login_required
def home(request):
    db_engine = connection.settings_dict['ENGINE'].split('.')[-1]
    return render(request, 'home.html', {
        'message': 'Привет: авторизация!',
        'db_info': f'PostgreSQL работает!'
    })