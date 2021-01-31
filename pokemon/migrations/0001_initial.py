# Generated by Django 3.1.5 on 2021-01-31 09:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PokemonType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('number', models.TextField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('devolution',
                 models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='evolutions',
                                   to='pokemon.pokemon')),
                ('types', models.ManyToManyField(to='pokemon.PokemonType')),
            ],
        ),
    ]