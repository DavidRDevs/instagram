# Generated by Django 5.1.2 on 2024-11-05 02:15

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='caption',
            field=ckeditor.fields.RichTextField(blank=True, max_length=500, verbose_name='Caption'),
        ),
    ]
