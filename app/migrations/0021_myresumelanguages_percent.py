# Generated by Django 4.1.6 on 2023-02-27 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_myresumeskills_percent'),
    ]

    operations = [
        migrations.AddField(
            model_name='myresumelanguages',
            name='percent',
            field=models.IntegerField(null=True),
        ),
    ]