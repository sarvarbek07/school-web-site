# Generated by Django 4.0.5 on 2023-03-13 16:11

from django.db import migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_alter_video_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video',
            field=embed_video.fields.EmbedVideoField(),
        ),
    ]
