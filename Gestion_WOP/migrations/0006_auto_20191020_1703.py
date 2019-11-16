# Generated by Django 2.2.6 on 2019-10-20 20:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Gestion_WOP', '0005_auto_20191020_1701'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='usuarioes',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Gestion_WOP.Usuario'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mensajes',
            name='clientees',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Gestion_WOP.Cliente'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mensajes',
            name='tmensajees',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Gestion_WOP.Tipo_Mensaje'),
            preserve_default=False,
        ),
    ]