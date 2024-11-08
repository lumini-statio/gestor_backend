# Generated by Django 4.2 on 2024-11-08 21:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("username", models.CharField(max_length=150, unique=True)),
                ("is_active", models.BooleanField(default=True)),
                ("is_staff", models.BooleanField(default=False)),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Mes",
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
                ("nombre", models.CharField(max_length=20)),
                ("sueldo_total", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "resultado",
                    models.DecimalField(decimal_places=2, default=0, max_digits=10),
                ),
                ("gasto_gas", models.DecimalField(decimal_places=2, max_digits=10)),
                ("gasto_luz", models.DecimalField(decimal_places=2, max_digits=10)),
                ("gasto_agua", models.DecimalField(decimal_places=2, max_digits=10)),
                ("gasto_comida", models.DecimalField(decimal_places=2, max_digits=10)),
                ("resto", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "expensas",
                    models.DecimalField(
                        blank=True, decimal_places=2, default=0, max_digits=10
                    ),
                ),
                (
                    "alquiler",
                    models.DecimalField(
                        blank=True, decimal_places=2, default=0, max_digits=10
                    ),
                ),
                (
                    "wifi",
                    models.DecimalField(
                        blank=True, decimal_places=2, default=0, max_digits=10
                    ),
                ),
                (
                    "usuario",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Gasto",
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
                ("nombre", models.CharField(default="", max_length=20)),
                (
                    "descripcion",
                    models.TextField(blank=True, default="", max_length=100, null=True),
                ),
                ("cantidad", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "mes",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="back.mes"
                    ),
                ),
                (
                    "usuario",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
