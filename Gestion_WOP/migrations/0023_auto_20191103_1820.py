# Generated by Django 2.2.6 on 2019-11-03 21:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Gestion_WOP', '0022_auto_20191103_1816'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='Password',
        ),
        migrations.AlterField(
            model_name='cliente',
            name='User',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
