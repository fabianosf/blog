# Generated by Django 4.0.6 on 2022-07-31 11:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0005_alter_comentario_usuario_comentario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='data_comentario',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
