from django.db import models
from django.contrib.auth.models import User
from systemModules.models import Company, Module
from django.conf import settings
import os
import pathlib


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор комментария', blank=True, null=True, related_name='comment_author')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='Компания', blank=True, null=True, related_name='comment_company')
    module = models.ForeignKey(Module, on_delete=models.CASCADE, verbose_name='Модуль', related_name='comment_module')
    record_id = models.IntegerField(verbose_name='Номер записи', blank=True, null=True)
    title = models.TextField(max_length=500, db_index=True, verbose_name='Содержимое')
    isPublished = models.BooleanField(default=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации', blank=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Комметарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['title']


class FileIcon(models.Model):
    title = models.CharField(blank=True, max_length=100, verbose_name='Наименование иконки')
    suffix = models.CharField(blank=True, max_length=100, verbose_name='Тип файла')
    icon_url = models.CharField(blank=True, max_length=100, verbose_name='Ссылка на иконку')

    class Meta:
        verbose_name = 'Иконки файлов'
        verbose_name_plural = 'Иконки файлов'
        ordering = ['-pk']

    def __str__(self):
        return self.title


class CommonFiles(models.Model):
    record_id = models.IntegerField(default=0, verbose_name='ID записи')
    module = models.ForeignKey(Module, blank=True, on_delete=models.CASCADE, verbose_name='Модуль', related_name='module_common_files')
    attached_file = models.FileField(upload_to='files/%Y/%m/%d', verbose_name='Файлы', blank=True)
    icon = models.ForeignKey('FileIcon', blank=True, on_delete=models.CASCADE, verbose_name='Иконка', related_name='icon_common_files')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Пользователь')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='Компания', blank=True, null=True,
                                related_name='common_files_company')
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата загрузки')

    class Meta:
        verbose_name='Файлы'
        verbose_name_plural='Файлы'
        ordering = ['pk']

    def __str__(self):
        return self.attached_file.name


    @property
    def file_parameters(self):
        try:
            file_size = os.path.getsize("media/" + str(self.attached_file))
            file_name = os.path.basename("media/" + str(self.attached_file))
            file_extension = pathlib.Path(file_name).suffix
        except:
            file_size = 0
            file_name = 0
            file_extension = 1

        context = {
            'file_size': file_size,
            'file_name': file_name,
            'file_extension': file_extension,
        }
        return context