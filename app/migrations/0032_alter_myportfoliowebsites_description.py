# Generated by Django 4.1.6 on 2023-02-28 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0031_remove_facebook_miss_link_remove_github_miss_link_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myportfoliowebsites',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
