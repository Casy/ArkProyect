# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='categorias',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('nombre', models.TextField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='publicaciones',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('path', models.TextField(max_length=2000)),
                ('nombre', models.TextField(max_length=512)),
                ('descripcion', models.TextField(max_length=1000)),
                ('fechaSubida', models.DateField(auto_now=True)),
                ('palabrasClave', models.TextField(max_length=1000)),
                ('visitas', models.IntegerField()),
                ('objetoUID', models.TextField(max_length=512)),
                ('flag', models.IntegerField()),
                ('categorias', models.ForeignKey(to='arkapp.categorias')),
            ],
        ),
        migrations.CreateModel(
            name='referencias',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('titulo', models.TextField(max_length=255)),
                ('fechaSubida', models.DateField(auto_now=True)),
                ('palabrasClave', models.TextField(max_length=1000)),
                ('texto', models.TextField(max_length=7900)),
                ('objetoUID', models.TextField(max_length=512)),
                ('flag', models.IntegerField()),
                ('publicaciones', models.ForeignKey(to='arkapp.publicaciones')),
            ],
        ),
        migrations.CreateModel(
            name='subCategorias',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('nombre', models.TextField(max_length=512)),
                ('categorias', models.ForeignKey(to='arkapp.categorias')),
            ],
        ),
        migrations.CreateModel(
            name='usuarios',
            fields=[
                ('id', models.AutoField(primary_key=True)),
                ('nombreUsuario', models.TextField(max_length=128, serialize=False, primary_key=True)),
                ('contrasena', models.TextField(max_length=128)),
                ('email', models.EmailField(max_length=128)),
                ('foto', sorl.thumbnail.fields.ImageField(upload_to=b'foto_usuario')),
                ('fechaAlta', models.DateField(auto_now=True)),
                ('flag', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='usuariosComplementos',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('atributo', models.TextField(max_length=100)),
                ('valor', models.TextField(max_length=100)),
                ('flagPublico', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='valoraciones',
            fields=[
                ('id', models.AutoField(primary_key=True)),
                ('objetoUID', models.TextField(max_length=128, serialize=False, primary_key=True)),
                ('valoracion', models.IntegerField()),
                ('usuarios', models.ForeignKey(to='arkapp.usuarios')),
            ],
        ),
        migrations.AddField(
            model_name='referencias',
            name='usuarios',
            field=models.ForeignKey(to='arkapp.usuarios'),
        ),
        migrations.AddField(
            model_name='publicaciones',
            name='subCategorias',
            field=models.ForeignKey(to='arkapp.subCategorias'),
        ),
        migrations.AddField(
            model_name='publicaciones',
            name='usuarios',
            field=models.ForeignKey(to='arkapp.usuarios'),
        ),
    ]
