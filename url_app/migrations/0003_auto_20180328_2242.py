# Generated by Django 2.0.2 on 2018-03-28 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url_app', '0002_urlshortener_shortcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urlshortener',
            name='shortcode',
            field=models.CharField(max_length=30),
        ),
    ]