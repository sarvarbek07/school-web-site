# Generated by Django 4.0.5 on 2023-03-10 08:55

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_blog_rasm'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='blog',
            managers=[
                ('user', django.db.models.manager.Manager()),
            ],
        ),
    ]
