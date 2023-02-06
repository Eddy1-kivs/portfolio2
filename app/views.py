from django.shortcuts import render, redirect
from . forms import *
from .models import *
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

# Create your views here.


def components(request):
    return render(request, 'components.html')


def index(request):
    welcome = Welcome.objects.all()
    coffee = CoffeeDrinked.objects.all()
    intouch = GetInTouch.objects.all()
    happy_clients = HappyClients.objects.all()
    worked_hours = HoursWorked.objects.all()
    expertise = MyExpertise.objects.all()
    r_education = MyResumeEducation.objects.all()
    r_expertise = MyResumeExpertise.objects.all()
    r_skills = MyResumeSkills.objects.all()
    r_languages = MyResumeLanguages.objects.all()
    services = MyServices.objects.all()
    p_info = PersonalInfo.objects.all()
    pro_finished = ProjectFinished.objects.all()
    send_message = SendAMessage.objects.all()
    am = WhoAmI.objects.all()
    ai = MyPortfolioAiAndMachineLearning.objects.all()
    app = MyPortfolioApps.objects.all()
    websites = MyPortfolioWebsites.objects.all()
    all_work = MyPortfolioALL.objects.all()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = SendAMessage(
                name=request.POST['name'],
                email=request.POST['email'],
                subject=request.POST['subject'],
                message=request.POST['message']
            )
            contact.save()
            messages.success(request,
                             'Your Message has been send successfully. I will get back to you soon Via Email.')

            # Define the message variable
            message = f"From: {contact.name}, Email: {contact.email}, Subject: {contact.subject}, Message: {contact.message}"

            # Send the email to multiple recipients
            recipients = ['kivuvaedwin@gmail.com']
            send_mail(contact.subject, message, 'settings.EMAIL_HOST_USER', recipients, fail_silently=False)
    else:
        form = ContactForm
        # return redirect('index')
    context = {
        'ai': ai,
        'app': app,
        'websites': websites,
        'all_work': all_work,
        'form': form,
        'welcome': welcome,
        'coffee': coffee,
        'intouch': intouch,
        'happy_clients': happy_clients,
        'worked_hours': worked_hours,
        'expertise': expertise,
        'r_education': r_education,
        'r_expertise': r_expertise,
        'r_skills': r_skills,
        'r_languages': r_languages,
        'services': services,
        'p_info': p_info,
        'pro_finished': pro_finished,
        'send_message': send_message,
        'am': am,
    }
    return render(request, 'index.html', context)

