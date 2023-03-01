from django.shortcuts import render, redirect
from . forms import *
from .models import *
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.views import View
# from validate_email import validate_email
from django.core.mail import EmailMessage
import json

# Create your views here.


def index(request):
    welcome = Welcome.objects.all()
    coffee = CoffeeDrank.objects.all()
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
    webservice = WebsiteService.objects.all()
    appservice = AppService.objects.all()
    aiandmachine = AIAndMachineService.objects.all()
    hire = HireMe.objects.all()
    facebook = Facebook.objects.all()
    twitter = Twitter.objects.all()
    linkedin = Linkedin.objects.all()
    instagram = Instagram.objects.all()
    github = Github.objects.all()
    background = HeaderBackground.objects.all()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = SendAMessage(
                name=request.POST['name'],
                email=request.POST['email'],
                message=request.POST['message']
            )
            contact.save()
            messages.success(request,
                             'Your Message has been send successfully. I will get back to you soon Via Email.')

            # Define the message variable
            message = f"From: {contact.name}, Email: {contact.email}, Message: {contact.message}"

            # Send the email to multiple recipients
            recipients = ['kivuvaedwin@gmail.com']
            send_mail(contact.name, message, 'settings.EMAIL_HOST_USER', recipients, fail_silently=False)
    else:
        form = ContactForm
    context = {
        'ai': ai,
        'app': app,
        'websites': websites,
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
        'webservice': webservice,
        'appservice': appservice,
        'aiandmachine': aiandmachine,
        'hire': hire,
        'facebook': facebook,
        'twitter': twitter,
        'github': github,
        'linkedin': linkedin,
        'instagram': instagram,
        'background': background,
    }
    return render(request, 'index.html', context)


def portfolio_detail(request, id):
    website = MyPortfolioWebsites.objects.filter(id=id).first()
    context = {
        'website': website,
    }
    return render(request, 'portfolio_detail.html', context)


class EmailValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        email = data['email']
        if not validate_email(email):
            return JsonResponse({'email_error': 'email is invalid'}, status=400)
        return JsonResponse({'email': True})


class RegistrationView(View):
    def get(self, request):
        return render(request, 'index.html')

    def post(self, request):
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        context = {
            'fieldValues': request.POST
        }
        if name < 2:
            messages.error(request, 'invalid name')
            return render(request, 'index.html', context)

        message = SendAMessage.objects.create(name=name, email=email, message=message)
        message.save()

        # Define the message variable
        message = f"From: {contact.name}, Email: {contact.email}, Message: {contact.message}"

        # Send the email to multiple recipients
        recipients = ['kivuvaedwin@gmail.com']
        send_mail(message, 'settings.EMAIL_HOST_USER', recipients, fail_silently=False)

        messages.success(request,  'Hi Message has been send successfully. I will get back to you soon Via Email.')

        return render(request, 'index.html')
