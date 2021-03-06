# Generated by Django 2.2.5 on 2019-11-22 06:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='file',
            field=models.ImageField(upload_to='food_photos'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='menu',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='menus.Menu'),
        ),
    ]
