# Generated by Django 2.2.6 on 2019-10-20 20:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Gestion_WOP', '0004_auto_20191020_1658'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='usuarioes',
        ),
        migrations.RemoveField(
            model_name='mensajes',
            name='clientees',
        ),
        migrations.RemoveField(
            model_name='mensajes',
            name='tmensajees',
        ),
    ]
