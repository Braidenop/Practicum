# Generated by Django 4.0 on 2022-01-13 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospA', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medico',
            name='ident',
            field=models.CharField(max_length=10, unique=True, verbose_name='Identificación'),
        ),
        migrations.AlterField(
            model_name='medico',
            name='num_te',
            field=models.CharField(max_length=10, verbose_name='Numero de Telefono'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='ident',
            field=models.CharField(max_length=10, unique=True, verbose_name='Identificación'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='num_te',
            field=models.CharField(max_length=10, verbose_name='Numero de Telefono'),
        ),
    ]
