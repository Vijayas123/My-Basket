# Generated by Django 2.2.6 on 2019-10-20 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=120, verbose_name='Username')),
                ('pwd', models.CharField(max_length=120, verbose_name='Password')),
                ('email', models.CharField(max_length=120, verbose_name='Email Id')),
                ('mobileno', models.CharField(max_length=120, verbose_name='Mobile no')),
                ('state', models.CharField(max_length=120, verbose_name='State')),
            ],
        ),
    ]