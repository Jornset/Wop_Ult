# Generated by Django 2.2.6 on 2019-10-25 04:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Gestion_WOP', '0014_auto_20191025_0053'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin_Pagina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserAdmin', models.CharField(max_length=50, unique=True)),
                ('PasswordAdmin', models.CharField(max_length=50)),
                ('AliasAdmin', models.CharField(max_length=50)),
                ('EmailAdmin', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name': 'Admin_Pagina',
                'verbose_name_plural': 'Admin_Paginas',
            },
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Titular', models.CharField(max_length=200)),
                ('Autor', models.CharField(max_length=100)),
                ('Cuerpo', models.CharField(max_length=10500)),
                ('Imagen', models.ImageField(null=True, upload_to='Noticias')),
                ('Link_YT', models.CharField(max_length=400, null=True)),
                ('Fecha_noticia', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'Noticia',
                'verbose_name_plural': 'Noticias',
            },
        ),
        migrations.AlterField(
            model_name='mensajes',
            name='Mensaje',
            field=models.CharField(max_length=1000),
        ),
        migrations.CreateModel(
            name='Comentarios_Noti',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Comentariocom', models.CharField(max_length=1500)),
                ('Fecha_comentario', models.DateTimeField()),
                ('Noticiacom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gestion_WOP.Noticia')),
                ('Usuariocom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gestion_WOP.Usuario')),
            ],
            options={
                'verbose_name': 'Comentario',
                'verbose_name_plural': 'Comentarios',
            },
        ),
    ]
