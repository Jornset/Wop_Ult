# Generated by Django 2.2.6 on 2019-10-19 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=30)),
                ('Email', models.EmailField(max_length=254)),
                ('Telefono', models.PositiveSmallIntegerField()),
                ('Ciudad', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Galeria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Descripcion', models.CharField(max_length=30)),
                ('Imagen', models.ImageField(upload_to='Photos')),
            ],
        ),
        migrations.CreateModel(
            name='Mensajes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Asunto', models.CharField(max_length=30)),
                ('Mensaje', models.CharField(max_length=150)),
            ],
        ),
    ]
