# Generated by Django 4.1.6 on 2023-02-27 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_myportfoliowebsites_image_4'),
    ]

    operations = [
        migrations.AddField(
            model_name='myresumeskills',
            name='percent',
            field=models.IntegerField(null=True),
        ),
    ]