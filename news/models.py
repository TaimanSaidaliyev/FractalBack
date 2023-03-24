from django.db import models
from django.contrib.auth.models import User
from systemModules.models import Company


class News(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    content = models.TextField(blank=True, null=True, verbose_name='Описание')
    company = models.ForeignKey(Company, blank=True, null=True, on_delete=models.CASCADE, verbose_name='Компания')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    photo = models.ImageField(upload_to='news/img/%Y/%m/%d', verbose_name='Изображение', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория', related_name='get_category')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор статьи', blank=True, null=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['title']


class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True, verbose_name='Категории')
    company = models.ForeignKey(Company, blank=True, null=True, on_delete=models.CASCADE, verbose_name='Компания')
    color = models.CharField(max_length=100, db_index=True, verbose_name='Цвет Bootstrap')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']