# Generated by Django 4.0.5 on 2023-03-10 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_remove_blog_rasm'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='rasm',
            field=models.ImageField(default='image/default.jpg', upload_to='image_blog'),
        ),
    ]
