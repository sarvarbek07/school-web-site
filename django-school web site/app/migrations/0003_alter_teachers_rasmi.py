# Generated by Django 4.0.5 on 2023-03-08 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_teachers_alter_about_image_alter_about_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teachers',
            name='rasmi',
            field=models.ImageField(upload_to='image'),
        ),
    ]