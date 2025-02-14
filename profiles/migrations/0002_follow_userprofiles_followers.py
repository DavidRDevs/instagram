# Generated by Django 5.1.2 on 2024-11-04 00:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='follow',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(
                    auto_now_add=True, verbose_name='¿Desde cuando lo sigue?')),
                ('follower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                 related_name='follower_set', to='profiles.UserProfiles', verbose_name='¿Quien sigue?')),
                ('following', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                 related_name='following_set', to='profiles.UserProfiles', verbose_name='¿A quien sigue?')),
            ],
            options={
                'verbose_name': 'Seguidor',
                'verbose_name_plural': 'Seguidores',
            },
        ),
        migrations.AddField(
            model_name='UserProfiles',
            name='followers',
            field=models.ManyToManyField(
                related_name='Following', through='profiles.follow', to='profiles.UserProfiles'),
        ),
    ]
