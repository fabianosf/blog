# Generated by Django 4.0.6 on 2022-07-31 07:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categorias', '0002_alter_categoria_nome_categoria'),
        ('posts', '0002_alter_post_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='categoria_post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='categorias.categoria', verbose_name='Categoria'),
        ),
        migrations.AlterField(
            model_name='post',
            name='conteudo_post',
            field=models.TextField(verbose_name='Conteudo'),
        ),
        migrations.AlterField(
            model_name='post',
            name='data_post',
            field=models.DateTimeField(verbose_name='Data'),
        ),
        migrations.AlterField(
            model_name='post',
            name='excerto_post',
            field=models.TextField(verbose_name='Excerto'),
        ),
        migrations.AlterField(
            model_name='post',
            name='imagem_post',
            field=models.ImageField(blank=True, null=True, upload_to='post_img/%Y/%m/%d', verbose_name='Imagem'),
        ),
        migrations.AlterField(
            model_name='post',
            name='titulo_post',
            field=models.CharField(max_length=255, verbose_name='Titulo'),
        ),
    ]