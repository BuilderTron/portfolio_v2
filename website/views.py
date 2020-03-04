from django.shortcuts import render
from django.core.mail import send_mail
# Create your views here.



def home(request):
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


        return render(request, 'home.html', {'name': name})

    else:
        return render(request, 'home.html', {})
