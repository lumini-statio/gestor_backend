# Generated by Django 5.0 on 2024-01-18 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0005_alter_mes_alquiler'),
    ]

    operations = [
        migrations.AddField(
            model_name='mes',
            name='wifi',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10),
        ),
    ]
