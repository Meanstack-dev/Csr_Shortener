# Generated by Django 2.0.2 on 2018-04-07 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url_app', '0008_auto_20180329_2003'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Full_Name', models.CharField(max_length=30)),
                ('Email', models.EmailField(max_length=30, unique=True)),
                ('Password', models.CharField(max_length=12)),
                ('Password_match', models.CharField(max_length=12)),
            ],
        ),
    ]
