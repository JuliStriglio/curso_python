# Generated by Django 4.2.5 on 2023-10-17 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0004_profesor_avatar_profesor_fecha_nac'),
    ]

    operations = [
        migrations.AddField(
            model_name='profesor',
            name='link',
            field=models.URLField(null=True),
        ),
    ]