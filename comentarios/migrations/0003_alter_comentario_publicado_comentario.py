# Generated by Django 4.0.6 on 2022-07-31 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0002_alter_comentario_comentario_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='publicado_comentario',
            field=models.BooleanField(default=False, verbose_name='Foi Publicado ??'),
        ),
    ]