# Generated by Django 4.2.5 on 2023-10-19 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0008_alter_profesor_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profesor',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatares'),
        ),
    ]