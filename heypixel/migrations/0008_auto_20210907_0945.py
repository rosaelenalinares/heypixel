# Generated by Django 2.2.13 on 2021-09-07 09:45

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('heypixel', '0007_auto_20210907_0937'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=cloudinary.models.CloudinaryField(default=True, max_length=255, verbose_name='image'),
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]