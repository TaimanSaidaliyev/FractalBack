# Generated by Django 4.1.6 on 2023-03-02 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0004_rename_module_name_commonfiles_module_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commonfiles',
            name='name',
        ),
        migrations.RemoveField(
            model_name='commonfiles',
            name='size',
        ),
        migrations.RemoveField(
            model_name='commonfiles',
            name='type',
        ),
    ]