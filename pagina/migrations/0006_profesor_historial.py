# Generated by Django 4.2.5 on 2023-10-18 20:10

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0005_profesor_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='profesor',
            name='historial',
            field=ckeditor.fields.RichTextField(default=1),
            preserve_default=False,
        ),
    ]