# Generated by Django 4.1.4 on 2022-12-29 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Livros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor', models.CharField(max_length=50)),
                ('editora', models.CharField(max_length=50)),
                ('isbn', models.IntegerField()),
                ('numeroPaginas', models.IntegerField()),
                ('titulo', models.CharField(max_length=50)),
                ('anoPublicacao', models.IntegerField()),
                ('emailEditora', models.EmailField(max_length=254)),
            ],
        ),
    ]