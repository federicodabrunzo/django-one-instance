# Generated by Django 3.2 on 2023-12-19 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_modelinheritanceexample'),
    ]

    operations = [
        migrations.CreateModel(
            name='PreExistingModelExample',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
