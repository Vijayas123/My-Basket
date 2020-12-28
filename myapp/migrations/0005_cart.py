# Generated by Django 2.2.6 on 2019-10-26 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=120, verbose_name='Username')),
                ('item_id', models.IntegerField(blank=True, default=1, null=True)),
            ],
        ),
    ]
