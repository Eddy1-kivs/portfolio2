# Generated by Django 4.1.6 on 2023-02-27 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_hireme_hire'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hireme',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='myportfolioaiandmachinelearning',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='myportfolioapps',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='myportfoliowebsites',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
