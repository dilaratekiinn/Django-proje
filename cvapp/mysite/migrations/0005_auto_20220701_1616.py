# Generated by Django 2.2 on 2022-07-01 13:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0004_advert_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Advert_User',
            new_name='AdvertUser',
        ),
    ]