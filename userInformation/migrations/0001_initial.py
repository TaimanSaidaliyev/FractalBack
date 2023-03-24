# Generated by Django 4.1.6 on 2023-02-12 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('systemModules', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('description', models.CharField(blank=True, max_length=100)),
                ('image', models.ImageField(blank=True, upload_to='img/certificates/%Y/%m/%d', verbose_name='Изображение сертификата')),
            ],
            options={
                'verbose_name': 'Сертификат',
                'verbose_name_plural': 'Сертификат',
                'ordering': ['-pk'],
            },
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=30)),
                ('description', models.CharField(blank=True, max_length=30)),
            ],
            options={
                'verbose_name': 'Пол',
                'verbose_name_plural': 'Пол',
                'ordering': ['-pk'],
            },
        ),
        migrations.CreateModel(
            name='Honor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('description', models.CharField(blank=True, max_length=100)),
                ('image', models.ImageField(blank=True, upload_to='img/honors/%Y/%m/%d', verbose_name='Изображение звания')),
            ],
            options={
                'verbose_name': 'Звание',
                'verbose_name_plural': 'Звание',
                'ordering': ['-pk'],
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('description', models.CharField(blank=True, max_length=100)),
                ('color', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'verbose_name': 'Статус',
                'verbose_name_plural': 'Статус',
                'ordering': ['-pk'],
            },
        ),
        migrations.CreateModel(
            name='JobTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('description', models.CharField(blank=True, max_length=100)),
                ('priority_number', models.IntegerField(blank=True, default=0, null=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='jobtitle_company', to='systemModules.company', verbose_name='Компания')),
            ],
            options={
                'verbose_name': 'Должность',
                'verbose_name_plural': 'Должность',
                'ordering': ['-pk'],
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('description', models.CharField(blank=True, max_length=100)),
                ('priority', models.IntegerField(blank=True, default=0)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='department_company', to='systemModules.company', verbose_name='Компания')),
            ],
            options={
                'verbose_name': 'Департамент',
                'verbose_name_plural': 'Департамент',
                'ordering': ['-pk'],
            },
        ),
    ]