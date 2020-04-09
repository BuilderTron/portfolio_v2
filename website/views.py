from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse
from .models import Project
# Create your views here.



def home(request):

    projects = Project.objects.all()

    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        #Send email
        send_mail(
        name,#Subject
        message,#Message
        email,#From Email
        ['jj.lopezbuilder@gmail.com'],#Email To

        )


        return render(request, 'home.html', {'name': name}, {'projects':projects})

    else:
        return render(request, 'home.html', {'projects':projects})
