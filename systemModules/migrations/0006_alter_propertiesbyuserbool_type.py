# Generated by Django 4.1.6 on 2023-02-19 04:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('systemModules', '0005_alter_propertiesbyuserbool_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertiesbyuserbool',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='property_type', to='systemModules.propertiesbyuserbool', verbose_name='Тип'),
        ),
    ]
