# Generated by Django 2.1.1 on 2018-10-10 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.SlugField(max_length=100, unique=True, verbose_name='Nombre clave')),
                ('name', models.CharField(max_length=200, verbose_name='Red social')),
                ('url', models.URLField(blank=True, null=True, verbose_name='Enlace')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha De Cración')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha De Edición')),
            ],
            options={
                'verbose_name': 'enlance',
                'verbose_name_plural': 'enlaces',
                'ordering': ['name'],
            },
        ),
    ]
