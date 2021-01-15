
from django.db import models
from datetime import date

from django.urls import reverse


class Footballers(models.Model):
    """Футболисты"""
    name = models.CharField(verbose_name="Имя", max_length=100)
    age = models.PositiveSmallIntegerField(verbose_name="Возраст", default=0)
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Футболисты"
        verbose_name_plural = "Футболисты"


class Club(models.Model):
    """Клуб"""
    title = models.CharField(verbose_name="Название", max_length=100)
    tagline = models.CharField(verbose_name="Слоган", max_length=100, default='')
    description = models.TextField(verbose_name="Описание")
    name = models.ManyToManyField(Footballers, verbose_name="Футболист", related_name="club_name")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("club_detail", kwargs={"slug": self.url})

    class Meta:
        verbose_name = "Клуб"
        verbose_name_plural = "Клубы"
# Create your models here.
