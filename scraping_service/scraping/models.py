from django.db import models

from scraping.utils import from_cyrillic_to_eng


class City(models.Model):
    """Sity in site"""

    name = models.CharField(max_length=50, verbose_name='Name of sity', unique=True, )
    slug = models.CharField(max_length=50, blank=True)

    class Meta:
        verbose_name = 'Name of sity'
        verbose_name_plural = "Name of sity's"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = from_cyrillic_to_eng(str(self.name))
            super().save(*args, **kwargs)


class Language(models.Model):
    name = models.CharField(max_length=50, verbose_name='Name of Language programming', unique=True, )
    slug = models.CharField(max_length=50, blank=True)

    class Meta:
        verbose_name = 'Name of Language programming'
        verbose_name_plural = "Name's of Language programming"

    def __str__(self):
        return self.name
