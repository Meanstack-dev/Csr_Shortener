# Generated by Django 2.0.2 on 2018-04-08 05:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('url_app', '0009_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]