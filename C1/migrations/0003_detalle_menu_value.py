# Generated by Django 5.0 on 2024-07-29 00:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("C1", "0002_alter_semana_semana"),
    ]

    operations = [
        migrations.AddField(
            model_name="detalle_menu",
            name="value",
            field=models.BooleanField(default=True),
        ),
    ]
