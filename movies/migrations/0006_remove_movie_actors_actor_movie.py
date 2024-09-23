# Generated by Django 5.0.6 on 2024-05-31 10:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_rename_casted_actors_movie_actors'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='actors',
        ),
        migrations.AddField(
            model_name='actor',
            name='movie',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='movies.movie'),
            preserve_default=False,
        ),
    ]
