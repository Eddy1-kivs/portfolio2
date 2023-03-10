# Generated by Django 4.1.6 on 2023-02-27 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0028_alter_hireme_hire_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Facebook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(max_length=100)),
                ('link', models.URLField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Facebook',
            },
        ),
        migrations.CreateModel(
            name='Github',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(max_length=100)),
                ('link', models.URLField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Github',
            },
        ),
        migrations.CreateModel(
            name='Instagram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(max_length=100)),
                ('link', models.URLField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Instagram',
            },
        ),
        migrations.CreateModel(
            name='Linkedin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(max_length=100)),
                ('link', models.URLField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Linkedin',
            },
        ),
        migrations.CreateModel(
            name='Twitter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(max_length=100)),
                ('link', models.URLField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Twitter',
            },
        ),
    ]
