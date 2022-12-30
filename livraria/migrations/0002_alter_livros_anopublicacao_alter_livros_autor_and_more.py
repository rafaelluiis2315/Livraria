# Generated by Django 4.1.4 on 2022-12-30 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livraria', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livros',
            name='anoPublicacao',
            field=models.IntegerField(verbose_name='Ano de Publicação'),
        ),
        migrations.AlterField(
            model_name='livros',
            name='autor',
            field=models.CharField(max_length=50, verbose_name='Autor'),
        ),
        migrations.AlterField(
            model_name='livros',
            name='editora',
            field=models.CharField(max_length=50, verbose_name='Editora'),
        ),
        migrations.AlterField(
            model_name='livros',
            name='emailEditora',
            field=models.EmailField(max_length=254, verbose_name='E-mail da Editora'),
        ),
        migrations.AlterField(
            model_name='livros',
            name='isbn',
            field=models.IntegerField(verbose_name='ISBN'),
        ),
        migrations.AlterField(
            model_name='livros',
            name='numeroPaginas',
            field=models.IntegerField(verbose_name='Número de Páginas'),
        ),
        migrations.AlterField(
            model_name='livros',
            name='titulo',
            field=models.CharField(max_length=50, verbose_name='Titulo'),
        ),
    ]
