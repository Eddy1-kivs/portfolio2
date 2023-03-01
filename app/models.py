from django.db import models

# Create your models here.


class Welcome(models.Model):
    name = models.CharField(max_length=100)
    specialisation = models.CharField(max_length=200)
    profile = models.ImageField(upload_to='media/profile', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Welcome'


class WhoAmI(models.Model):
    Title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.Title

    class Meta:
        verbose_name_plural = 'Who Am I'


class PersonalInfo(models.Model):
    birthdate = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    Upwork = models.CharField(max_length=100)
    skype = models.CharField(max_length=100)

    def __str__(self):
        return self.birthdate

    class Meta:
        verbose_name_plural = 'Personal Info'


class MyExpertise(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    icon = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'My Expertise'


class MyResumeExpertise(models.Model):
    time = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'My Resume Expertise'


class MyResumeEducation(models.Model):
    time = models.CharField(max_length=100)
    school_name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.school_name

    class Meta:
        verbose_name_plural = 'My Resume Education'


class MyResumeSkills(models.Model):
    programming_language = models.CharField(max_length=100)
    percent = models.IntegerField(null=True)

    def __str__(self):
        return self.programming_language

    class Meta:
        verbose_name_plural = 'My Resume Skills'


class MyResumeLanguages(models.Model):
    language = models.CharField(max_length=100)
    percent = models.IntegerField(null=True)

    def __str__(self):
        return self.language

    class Meta:
        verbose_name_plural = 'My Resume Languages'


class HoursWorked(models.Model):
    hours = models.CharField(max_length=100)

    def __str__(self):
        return self.hours

    class Meta:
        verbose_name_plural = 'Hours Worked'


class ProjectFinished(models.Model):
    projects = models.CharField(max_length=100)

    def __str__(self):
        return self.projects

    class Meta:
        verbose_name_plural = 'Projects Finished'


class HappyClients(models.Model):
    happy = models.CharField(max_length=100)

    def __str__(self):
        return self.happy

    class Meta:
        verbose_name_plural = 'Happy Clients'


class CoffeeDrank(models.Model):
    coffee = models.CharField(max_length=100)

    def __str__(self):
        return self.coffee

    class Meta:
        verbose_name_plural = 'Coffee Drank'


class MyServices(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'My Services'


class MyPortfolioWebsites(models.Model):
    name_of_site = models.CharField(max_length=100)
    link = models.URLField(blank=True, null=True)
    miss_link = models.CharField(blank=True, max_length=100, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='media/websites')
    image_1 = models.ImageField(upload_to='media/websites', null=True)
    image_2 = models.ImageField(upload_to='media/websites', null=True)
    image_3 = models.ImageField(upload_to='media/websites', null=True)
    image_4 = models.ImageField(upload_to='media/websites', null=True)
    image_5 = models.ImageField(upload_to='media/websites', null=True)
    image_6 = models.ImageField(upload_to='media/websites', null=True)
    image_7 = models.ImageField(upload_to='media/websites', null=True)
    image_8 = models.ImageField(upload_to='media/websites', null=True)

    def __str__(self):
        return self.name_of_site

    class Meta:
        verbose_name_plural = 'Websites'


class MyPortfolioApps(models.Model):
    image = models.ImageField()
    name_of_site = models.CharField(max_length=100)
    link = models.URLField(blank=True, null=True)
    miss_link = models.CharField(blank=True, max_length=100, null=True)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name_of_site

    class Meta:
        verbose_name_plural = 'Mobile Apps'


class MyPortfolioAiAndMachineLearning(models.Model):
    image = models.ImageField()
    name_of_site = models.CharField(max_length=100)
    link = models.URLField(blank=True, null=True)
    miss_link = models.CharField(blank=True, max_length=100, null=True)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name_of_site

    class Meta:
        verbose_name_plural = 'AI and Machine Learning'


class SendAMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = 'Messages'


class GetInTouch(models.Model):
    phone_number = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = 'Get In Touch'


class WebsiteService(models.Model):
    icon = models.CharField(max_length=100, null=True)
    title = models.CharField(max_length=200, null=True)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Website Service'


class AppService(models.Model):
    icon = models.CharField(max_length=100, null=True)
    title = models.CharField(max_length=200, null=True)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'App Service'


class AIAndMachineService(models.Model):
    icon = models.CharField(max_length=100, null=True)
    title = models.CharField(max_length=200, null=True)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Ai and Machine learning Service'


class HireMe(models.Model):
    heading = models.CharField(max_length=100)
    link = models.URLField(blank=True, null=True)
    miss_link = models.CharField(max_length=100, null=True)
    hire = models.CharField(blank=True, max_length=100, null=True)

    def __str__(self):
        return self.heading

    class Meta:
        verbose_name_plural = 'Hire Me'


class Facebook(models.Model):
    icon = models.CharField(max_length=100)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.icon

    class Meta:
        verbose_name_plural = "Facebook"


class Linkedin(models.Model):
    icon = models.CharField(max_length=100)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.icon

    class Meta:
        verbose_name_plural = "Linkedin"


class Twitter(models.Model):
    icon = models.CharField(max_length=100)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.icon

    class Meta:
        verbose_name_plural = "Twitter"


class Github(models.Model):
    icon = models.CharField(max_length=100)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.icon

    class Meta:
        verbose_name_plural = "Github"


class Instagram(models.Model):
    icon = models.CharField(max_length=100)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.icon

    class Meta:
        verbose_name_plural = "Instagram"


class HeaderBackground(models.Model):
    image = models.ImageField(upload_to='media/background', null=True)

    # def __str__(self):
        # return self.image

    class Meta:
        verbose_name_plural = "Header Background"