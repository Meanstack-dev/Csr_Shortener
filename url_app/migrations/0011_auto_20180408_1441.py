# Generated by Django 2.0.2 on 2018-04-08 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url_app', '0010_delete_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urlshortener',
            name='shortcode',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]