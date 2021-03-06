# Generated by Django 2.1.2 on 2018-10-20 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passengerAPI', '0004_auto_20181021_0049'),
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=80)),
                ('last_name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=200)),
                ('number', models.IntegerField(unique=True)),
                ('license', models.CharField(max_length=80, unique=True)),
                ('car_no', models.CharField(max_length=80, unique=True)),
            ],
        ),
    ]
