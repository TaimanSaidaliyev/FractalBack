# Generated by Django 4.1.6 on 2023-02-25 06:28

from django.db import migrations
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('projectManagement', '0003_alter_tasks_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='children', to='projectManagement.tasks'),
        ),
    ]
