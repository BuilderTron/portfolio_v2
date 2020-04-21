from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def rpg(request):
    return render(request, 'random_password_generator/rpg.html',{})
