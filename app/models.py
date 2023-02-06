from django.db import models

# Create your models here.


class Welcome(models.Model):
    name = models.CharField(max_length=100)
    specialisation = models.CharField(max_length=200)
    background = models.ImageField(upload_to='background_image')

    def __str__(self):
        return self.name


class WhoAmI(models.Model):
    Title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.Title


class PersonalInfo(models.Model):
    birthdate = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    Upwork = models.CharField(max_length=100)
    skype = models.CharField(max_length=100)

    def __str__(self):
        return self.birthdate


class MyExpertise(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class MyResumeExpertise(models.Model):
    # title = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class MyResumeEducation(models.Model):
    # title = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    school_name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.school_name


class MyResumeSkills(models.Model):
    # title = models.CharField(max_length=100)
    programming_language = models.CharField(max_length=100)
    # rating = models.FloatField()
    # ip = models.CharField(max_length=20, blank=True)
    # status = models.BooleanField(default=True)

    def __str__(self):
        return self.programming_language


class MyResumeLanguages(models.Model):
    language = models.CharField(max_length=100)
    # level = models.

    def __str__(self):
        return self.language


class HoursWorked(models.Model):
    hours = models.CharField(max_length=100)

    def __str__(self):
        return self.hours


class ProjectFinished(models.Model):
    projects = models.CharField(max_length=100)

    def __str__(self):
        return self.projects


class HappyClients(models.Model):
    happy = models.CharField(max_length=100)

    def __str__(self):
        return self.happy


class CoffeeDrinked(models.Model):
    coffee = models.CharField(max_length=100)

    def __str__(self):
        return self.coffee


class MyServices(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class MyPortfolioALL(models.Model):
    image = models.ImageField()
    name_of_site = models.CharField(max_length=100)
    link = models.CharField(max_length=200)

    def __str__(self):
        return self.name_of_site


class MyPortfolioWebsites(models.Model):
    image = models.ImageField()
    name_of_site = models.CharField(max_length=100)
    link = models.CharField(max_length=200)

    def __str__(self):
        return self.name_of_site


class MyPortfolioApps(models.Model):
    image = models.ImageField()
    name_of_site = models.CharField(max_length=100)
    link = models.CharField(max_length=200)

    def __str__(self):
        return self.name_of_site


class MyPortfolioAiAndMachineLearning(models.Model):
    image = models.ImageField()
    name_of_site = models.CharField(max_length=100)
    link = models.CharField(max_length=200)

    def __str__(self):
        return self.name_of_site


class SendAMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100,null=True)
    message = models.TextField()

    def __str__(self):
        return self.email


class GetInTouch(models.Model):
    phone_number = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.email
