# Generated by Django 5.1.4 on 2024-12-24 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(upload_to='avatars/'),
        ),
    ]
