# Generated by Django 5.0.4 on 2024-04-25 08:55

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="EnergyPrice",
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
                ("date", models.DateField()),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("country_code", models.CharField(max_length=2)),
            ],
        ),
    ]