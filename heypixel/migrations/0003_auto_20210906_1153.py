# Generated by Django 2.2.13 on 2021-09-06 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('heypixel', '0002_auto_20210906_0947'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='picture',
            new_name='image',
        ),
    ]