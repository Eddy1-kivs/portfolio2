# Generated by Django 4.1.6 on 2023-02-26 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_myportfolioaiandmachinelearning_image_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MyPortfolioALL',
        ),
        migrations.AlterModelOptions(
            name='coffeedrinked',
            options={'verbose_name_plural': 'Coffee Drinked'},
        ),
        migrations.AlterModelOptions(
            name='getintouch',
            options={'verbose_name_plural': 'Get In Touch'},
        ),
        migrations.AlterModelOptions(
            name='happyclients',
            options={'verbose_name_plural': 'Happy Clients'},
        ),
        migrations.AlterModelOptions(
            name='hoursworked',
            options={'verbose_name_plural': 'Hours Worked'},
        ),
        migrations.AlterModelOptions(
            name='myexpertise',
            options={'verbose_name_plural': 'My Expertise'},
        ),
        migrations.AlterModelOptions(
            name='myportfolioaiandmachinelearning',
            options={'verbose_name_plural': 'AI and Machine Learning'},
        ),
        migrations.AlterModelOptions(
            name='myportfolioapps',
            options={'verbose_name_plural': 'Mobile Apps'},
        ),
        migrations.AlterModelOptions(
            name='myportfoliowebsites',
            options={'verbose_name_plural': 'Websites'},
        ),
        migrations.AlterModelOptions(
            name='myresumeeducation',
            options={'verbose_name_plural': 'My Resume Education'},
        ),
        migrations.AlterModelOptions(
            name='myresumeexpertise',
            options={'verbose_name_plural': 'My Resume Expertise'},
        ),
        migrations.AlterModelOptions(
            name='myresumelanguages',
            options={'verbose_name_plural': 'My Resume Languages'},
        ),
        migrations.AlterModelOptions(
            name='myresumeskills',
            options={'verbose_name_plural': 'My Resume Skills'},
        ),
        migrations.AlterModelOptions(
            name='myservices',
            options={'verbose_name_plural': 'My Services'},
        ),
        migrations.AlterModelOptions(
            name='personalinfo',
            options={'verbose_name_plural': 'Personal Info'},
        ),
        migrations.AlterModelOptions(
            name='projectfinished',
            options={'verbose_name_plural': 'Projects Finished'},
        ),
        migrations.AlterModelOptions(
            name='sendamessage',
            options={'verbose_name_plural': 'Messages'},
        ),
        migrations.AlterModelOptions(
            name='welcome',
            options={'verbose_name_plural': 'Welcome'},
        ),
        migrations.AlterModelOptions(
            name='whoami',
            options={'verbose_name_plural': 'Who Am I'},
        ),
        migrations.AddField(
            model_name='myportfolioaiandmachinelearning',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='myportfolioapps',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='myportfoliowebsites',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
