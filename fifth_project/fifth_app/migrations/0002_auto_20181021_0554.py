# Generated by Django 2.1.1 on 2018-10-21 05:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fifth_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofileinfo',
            old_name='portfolio_pic',
            new_name='profile_pic',
        ),
    ]
