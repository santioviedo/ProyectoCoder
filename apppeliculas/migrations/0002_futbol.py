# Generated by Django 4.2.8 on 2024-01-08 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apppeliculas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='futbol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipo_local', models.CharField(max_length=40)),
                ('equipo_visitante', models.CharField(max_length=40)),
                ('resultado', models.CharField(max_length=40)),
                ('fecha', models.DateField()),
            ],
        ),
    ]
