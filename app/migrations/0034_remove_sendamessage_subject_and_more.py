# Generated by Django 4.1.6 on 2023-03-01 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0033_headerbackground'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sendamessage',
            name='subject',
        ),
        migrations.AlterField(
            model_name='headerbackground',
            name='image',
            field=models.ImageField(null=True, upload_to='media/background'),
        ),
    ]
