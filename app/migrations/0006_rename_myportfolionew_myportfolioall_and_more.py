# Generated by Django 4.1.5 on 2023-01-28 07:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_sendamessage_subject'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MyPortfolioNew',
            new_name='MyPortfolioALL',
        ),
        migrations.DeleteModel(
            name='LatestTechNews',
        ),
    ]