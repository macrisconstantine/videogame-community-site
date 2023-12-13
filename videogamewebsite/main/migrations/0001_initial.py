# Generated by Django 4.2.7 on 2023-12-13 13:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import main.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, null=True, unique=True, verbose_name='Genre slug')),
                ('image', models.ImageField(max_length=255, upload_to=main.models.Genre.image_upload_to)),
            ],
            options={
                'verbose_name_plural': 'Genres',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='SubGenre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('subgenre_slug', models.SlugField(blank=True, null=True, unique=True, verbose_name='Subgenre slug')),
                ('image', models.ImageField(max_length=255, upload_to=main.models.SubGenre.image_upload_to)),
                ('genre', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.genre')),
            ],
            options={
                'verbose_name_plural': 'Subgenres',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='VideoGame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('platform', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('release_date', models.DateField()),
                ('game_slug', models.SlugField(unique=True, verbose_name='Game slug')),
                ('image', models.ImageField(max_length=255, upload_to=main.models.VideoGame.image_upload_to)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.genre')),
                ('subgenre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.subgenre')),
            ],
            options={
                'verbose_name_plural': 'Video games',
                'ordering': ['-release_date'],
            },
        ),
    ]
