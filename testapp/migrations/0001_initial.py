# Generated by Django 3.2.14 on 2023-12-05 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enabled', models.BooleanField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SMTPConfigs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host', models.CharField(max_length=1024, verbose_name='SMTP Host')),
                ('port', models.PositiveSmallIntegerField(default=587, verbose_name='SMTP Port')),
                ('username', models.CharField(max_length=255, verbose_name='Username')),
                ('password', models.CharField(max_length=255, verbose_name='Password')),
                ('use_tls', models.BooleanField(default=True, verbose_name='Use TLS')),
                ('use_ssl', models.BooleanField(default=True, verbose_name='Use SSL')),
                ('from_email', models.EmailField(max_length=254, verbose_name='From Email')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
