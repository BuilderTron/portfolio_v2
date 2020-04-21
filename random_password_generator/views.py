from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.
def rpg(request):
    return render(request, 'random_password_generator/rpg.html',{})


def about_us(request):
    return render(request, 'random_password_generator/about_us.html')


def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYS'))

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*'))

    length = int(request.GET.get('length',12))
    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'random_password_generator/password.html', {'password':thepassword})
