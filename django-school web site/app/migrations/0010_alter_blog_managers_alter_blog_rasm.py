# Generated by Django 4.0.5 on 2023-03-11 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_blog_managers'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='blog',
            managers=[
            ],
        ),
        migrations.AlterField(
            model_name='blog',
            name='rasm',
            field=models.ImageField(upload_to='image_blog'),
        ),
    ]
