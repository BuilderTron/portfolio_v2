from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse
from .models import Project, Resume
# Create your views here.



def home(request):

    projects = Project.objects.all().order_by('-created')
    resumes = Resume.objects.all()


    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        msg_mail = "Name: " + str(name) + "\n\nEmail: " + str(email) + "\n\nMessage: " + str(message)


        #Send email
        send_mail(
            'Portfolio: ' + name,
            msg_mail,
            email,
            ['jj.lopezbuilder@gmail.com'],#Email To
            fail_silently=False,
        )



        return render(request, 'website/home.html', {'name': name, 'projects':projects, 'resumes':resumes})

    else:
        return render(request, 'website/home.html', {'projects':projects, 'resumes':resumes})
