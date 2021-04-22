from django.shortcuts import render, redirect
from pages.models import Team
from place.models import Place
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
def home(request):
    teams = Team.objects.all()
    trending_place = Place.objects.order_by('-added_date').filter(is_trending=True)
    recommended_place = Place.objects.order_by('-added_date').filter(is_recommended=True)
    data = {'teams': teams, 'recommended_place':recommended_place, 'trending_place':trending_place}
    return render(request,'pages/home.html',data)

def about(request):
    teams = Team.objects.all()
    data = {'teams':teams}
    return render(request,'pages/about.html',data)

def community(request):
    return render(request,'pages/community.html')
    
    
def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']

        email_subject = 'You have a new message from Mytour website regarding' + subject
        message_body = 'Name: '+ name + '. Email: ' + email + '. Phone: ' + phone + '. Message: ' + message

        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email

        send_mail(
            email_subject,
            message_body,
            'gauravmyntra097@gmail.com',
            [admin_email],
            fail_silently=False,
        )
        messages.success(request,'Thank you for contacting us. We will get back to you shortly.')
        return redirect('contact')

    return render(request,'pages/contact.html')