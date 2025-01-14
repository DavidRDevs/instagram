# Generated by Django 5.1.2 on 2024-11-03 21:47

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', models.ImageField(blank=True, null=True,
                 upload_to='profile_pictures/', verbose_name='Imagen de perfil')),
                ('bio', models.TextField(blank=True,
                 max_length=500, verbose_name='Biografia')),
                ('birth_date', models.DateField(blank=True,
                 null=True, verbose_name='Fecha de nacimiento')),
                ('created_at', models.DateTimeField(blank=True, default=django.utils.timezone.now,
                 null=True, verbose_name='Fecha y Hora de creación')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE,
                 related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profiles',
            },
        ),
    ]
