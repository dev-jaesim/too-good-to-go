# Generated by Django 2.2.5 on 2019-11-22 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('businesses', '0002_business_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='business_photo'),
        ),
    ]
