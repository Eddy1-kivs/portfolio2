# Generated by Django 4.1.5 on 2023-01-30 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_myportfolioaiandmachinelearning_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myportfolioaiandmachinelearning',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='myportfolioall',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='myportfolioapps',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='myportfoliowebsites',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
