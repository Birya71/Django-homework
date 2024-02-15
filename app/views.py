
from django.http import HttpResponse
from django.shortcuts import render, reverse
import datetime as dt
import os


def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }

    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    template_name = 'app/time.html'
    current_time = dt.datetime.now()
    msg = current_time.strftime('%H:%M - %m.%d.%Y года')
    # msg = f'Текущее время: {current_time}'
    context = {
        'time': msg
    }
    return render(request, template_name, context)


def workdir_view(request):
    template_name = 'app/workdir.html'
    workdir = os.listdir('C:/Data/Django/dj-homeworks-video/1.1-first-project/first_project/app')
    # print(workdir)
    context = {
        'workdir': workdir
    }
    return render(request, template_name, context)