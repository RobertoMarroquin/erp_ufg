# Generated by Django 5.1.2 on 2024-10-26 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='fecha_vencimiento',
            field=models.DateField(blank=True, null=True),
        ),
    ]
