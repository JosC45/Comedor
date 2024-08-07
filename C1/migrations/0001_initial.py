# Generated by Django 5.0 on 2024-07-24 23:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Alumno",
            fields=[
                (
                    "codigo",
                    models.CharField(max_length=8, primary_key=True, serialize=False),
                ),
                ("nombres", models.CharField(max_length=50)),
                ("apellidos", models.CharField(max_length=50)),
                ("Carrera", models.CharField(max_length=30)),
                ("Estado", models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name="Dia",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("dia", models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="Semana",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("semana", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Tipo_Menu",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("tipo", models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="Menu",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("bebida", models.CharField(max_length=30)),
                ("comida", models.CharField(max_length=30)),
                (
                    "id_dia",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="C1.dia"
                    ),
                ),
                (
                    "id_semana",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="C1.semana"
                    ),
                ),
                (
                    "id_tipo",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="C1.tipo_menu"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="detalle_menu",
            fields=[
                (
                    "id_detalle_menu",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                (
                    "codigo",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="C1.alumno"
                    ),
                ),
                (
                    "id_menu",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="C1.menu"
                    ),
                ),
            ],
        ),
    ]
