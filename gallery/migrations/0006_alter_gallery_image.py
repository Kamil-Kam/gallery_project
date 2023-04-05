# Generated by Django 4.1.7 on 2023-04-01 08:17

from django.db import migrations
import django_resized.forms
import gallery.models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0005_alter_gallery_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=None, force_format='JPEG', keep_meta=True, quality=75, scale=0.5, size=[3840, 3840], upload_to=gallery.models.get_image_path),
        ),
    ]
