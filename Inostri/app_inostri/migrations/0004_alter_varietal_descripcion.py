# Generated by Django 4.2.1 on 2023-05-22 19:46

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_inostri', '0003_rename_region_bodega_zona_rename_region_vino_zona'),
    ]

    operations = [
        migrations.AlterField(
            model_name='varietal',
            name='descripcion',
            field=ckeditor.fields.RichTextField(default=''),
        ),
    ]
