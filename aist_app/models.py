# -*- coding: utf-8 -*-

from django.db import models
from tinymce import models as tinymce_models


class IndexPicture(models.Model):
    url = models.URLField(u'ссылка')
    name = models.CharField(u'Название фото', max_length=150, blank=True, null=True)
    descr = models.TextField(u'Описание фото', blank=True, null=True)
    position = models.SmallIntegerField(u'Порядок следования')
    
    class Meta:
        ordering = ['position',]
        verbose_name = u'Фото на главной странице'
        verbose_name_plural = u'фото на главной странице'


class Manufacturer(models.Model):
    name = models.CharField(u'Название', max_length=250)
    url = models.URLField(u'ссылка на сайт')
    position = models.SmallIntegerField(u'Порядок следования')

    class Meta:
        ordering = ['position',]
        verbose_name = u'Производитель оборудования'
        verbose_name_plural = u'производители оборудования'

    def __unicode__(self):
        return self.name


class CompanyText(models.Model):
    header = models.CharField(u'Заголовок', max_length=150)
    hello_text = models.TextField(u'Текст приветствия')
    about = tinymce_models.HTMLField(u'О компании')
    activity = tinymce_models.HTMLField(u'Виды деятельности')


    class Meta:
        verbose_name = u'Текстовая информация о компании'
        verbose_name_plural = u'текстовая информация о компании'

    def __unicode__(self):
        return self.header


class Certificate(models.Model):
    name = models.CharField(u'Название', max_length=250)
    url = models.URLField(u'ссылка')
    thumbnail_url = models.URLField(u'ссылка на превью', blank=True, null=True)
    #content_type = models.ForeignKey(ContentType)
    #object_id = models.PositiveIntegerField()
    #content_object = generic.GenericForeignKey('content_type', 'object_id')
    
    #def natural_key(self):
    #    return (self.name, self.url, self.thumbnail_url)

    class Meta:
        verbose_name = u'Сертификат'
        verbose_name_plural = u'сертификаты'
    
    def __unicode__(self):
        return self.name


class New(models.Model):
    title = models.CharField(u'Заголовок', max_length=150)
    short_text = tinymce_models.HTMLField(u'Краткое содержание')
    full_text = tinymce_models.HTMLField(u'Полный текст')
    date_added = models.DateField(u'Дата добавления')
    big_new = models.BooleanField(u'Новость с отдельной страницей ?', default=False)
    
    class Meta:
        ordering = ['-date_added']
        verbose_name = u'Новость'
        verbose_name_plural = u'новости'
    
    def __unicode__(self):
        return self.title


class Picture(models.Model):
    name = models.CharField(u'Название', max_length=250)
    new = models.ForeignKey(New, related_name='pictures_list')
    position = models.SmallIntegerField(u'Порядок следования')
    url = models.URLField(u'ссылка')

    class Meta:
        ordering = ['position',]
        verbose_name = u'Фото'
        verbose_name_plural = u'фото'
    
    def __unicode__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(u'Название', max_length=250)    
    description = tinymce_models.HTMLField(u'Описание услуги')

    class Meta:
        verbose_name = u'Услуга'
        verbose_name_plural = u'услуги'
    
    def __unicode__(self):
        return self.name


class Document(models.Model):
    name = models.CharField(u'Название', max_length=250)
    url = models.URLField(u'ссылка')
    position = models.SmallIntegerField(u'Порядок следования')
    # content_type = models.ForeignKey(ContentType)
    # object_id = models.PositiveIntegerField()
    # content_object = generic.GenericForeignKey('content_type', 'object_id')
    
    # def natural_key(self):
    #     return (self.name, self.url)
    
    class Meta:
        verbose_name = u'Документ'
        verbose_name_plural = u'документы'
    
    def __unicode__(self):
        return self.name


class Contacts(models.Model):
    contacts = tinymce_models.HTMLField(u'Контакты')

    class Meta:
        verbose_name = u'Контакты'
        verbose_name_plural = u'контакты'
    
    def __unicode__(self):
        return u'Контакты'


class Question(models.Model):
    last_name = models.CharField(u'Имя', max_length=100)
    first_name = models.CharField(u'Фамилия', max_length=100)
    email = models.EmailField(u'E-mail', max_length=100)
    subject = models.CharField(u'Тема', max_length=100, blank=True, null=True)
    question = models.TextField(u'Вопрос')

    class Meta:
        verbose_name = u'Вопрос'
        verbose_name_plural = u'вопросы'
    
    def __unicode__(self):
        return u'%s %s - %s' % (self.last_name, self.first_name, self.subject)
