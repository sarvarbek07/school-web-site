# Generated by Django 4.0.5 on 2023-03-09 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_teachers_rasmi'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rasm', models.ImageField(upload_to='image_blog')),
                ('sarlafha', models.CharField(max_length=300)),
                ('matn', models.TextField()),
                ('vaqt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]