# Generated by Django 4.1.6 on 2023-02-19 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('systemModules', '0007_alter_propertiesbyuserbool_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertiesbyuserbool',
            name='isBool',
            field=models.BooleanField(default=True, verbose_name='TrueFalse'),
        ),
    ]