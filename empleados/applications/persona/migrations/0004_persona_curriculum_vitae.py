# Generated by Django 3.2.7 on 2021-09-13 02:40

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0003_auto_20210912_2117'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='curriculum_vitae',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Hoja de vida'),
        ),
    ]