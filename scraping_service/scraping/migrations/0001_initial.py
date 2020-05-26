# Generated by Django 3.0.6 on 2020-05-26 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Name of sity')),
                ('slug', models.CharField(blank=True, max_length=50)),
            ],
            options={
                'verbose_name': 'Name of sity',
                'verbose_name_plural': "Name of sity's",
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Name of Language programming')),
                ('slug', models.CharField(blank=True, max_length=50)),
            ],
            options={
                'verbose_name': 'Name of Language programming',
                'verbose_name_plural': "Name's of Language programming",
            },
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(unique=True)),
                ('title', models.CharField(max_length=250, verbose_name='Vacancy title')),
                ('company', models.CharField(max_length=250, verbose_name='Company')),
                ('description', models.TextField(verbose_name='Description vacancy')),
                ('timestamp', models.DateField(auto_now_add=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scraping.City', verbose_name='City')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scraping.Language', verbose_name='Programing language')),
            ],
            options={
                'verbose_name': 'Vacancy in Site',
                'verbose_name_plural': "Vacancy's in Site",
            },
        ),
    ]
