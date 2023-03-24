from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    title = models.CharField(max_length=100, db_index=True, verbose_name='Название компании')
    active = models.BooleanField(default=False, blank=True, null=True)
    logotype = models.ImageField(upload_to='company/img/logotype/%Y/%m/%d', verbose_name='Логотип компании', blank=True)
    logo_dark_mode = models.ImageField(upload_to='company/img/logotype/%Y/%m/%d', verbose_name='Логотип для темной версии', blank=True)
    logo_light_mode = models.ImageField(upload_to='company/img/logotype/%Y/%m/%d', verbose_name='Логотип для светлой версии', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'
        ordering = ['title']


class Module(models.Model):
    title = models.CharField(max_length=100, db_index=True, verbose_name='Название модуля')
    slug = models.CharField(max_length=100, db_index=True, verbose_name='Техническое название')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Модуль'
        verbose_name_plural = 'Модули'
        ordering = ['title']


class PropertiesByUserBool(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор статьи', blank=True, null=True)
    module = models.ForeignKey('Module', on_delete=models.CASCADE, verbose_name='Модуль', related_name='property_module')
    record_id = models.IntegerField(verbose_name='Номер записи', blank=True, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='Компания', blank=True, null=True,
                                related_name='property_company')
    type = models.ForeignKey('TypeOfPropertiesByUserBool', on_delete=models.CASCADE, verbose_name='Тип', related_name='property_type')
    isBool = models.BooleanField(verbose_name='TrueFalse', default=True)

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = 'Свойства'
        verbose_name_plural = 'Свойства'
        ordering = ['user']


class TypeOfPropertiesByUserBool(models.Model):
    title = models.CharField(blank=True, default='', verbose_name='Название', max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тип свойства'
        verbose_name_plural = 'Тип свойства'
        ordering = ['title']