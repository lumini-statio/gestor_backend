# Generated by Django 4.2 on 2024-01-24 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0007_gasto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gasto',
            name='descripcion',
            field=models.TextField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='gasto',
            name='nombre',
            field=models.CharField(default='', max_length=20),
        ),
    ]
