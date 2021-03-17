from django.db import models

from .utils import convert_from_cyrillic_to_eng


class City(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название населенного пункта', unique=True)
    slug = models.SlugField(max_length=50, blank=True, unique=True)

    class Meta:
        verbose_name = 'Название населенного пункта'
        verbose_name_plural = 'Названия населенных пунктов'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = convert_from_cyrillic_to_eng(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=50, verbose_name='Язык программирования', unique=True)
    slug = models.SlugField(max_length=50, blank=True, unique=True)

    class Meta:
        verbose_name = 'Язык программирования'
        verbose_name_plural = 'Языки программирования'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = convert_from_cyrillic_to_eng(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name