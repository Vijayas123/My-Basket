# Generated by Django 2.2.6 on 2019-10-24 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_items'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Customer',
        ),
    ]