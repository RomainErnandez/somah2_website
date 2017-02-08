from django.db import models
from django_countries.fields import CountryField

# Create your models here.

class Language(models.Model):
    name = models.CharField(max_length=20)
    country = CountryField(primary_key=True) # code: ISO 639-1

    def __str__(self):
        return self.name

class Period(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True) # periods will be in id's order
    image = models.ImageField(default='0011ff.png')

    def __str__(self):
        return str(self.id)

class PeriodTr(models.Model):
    name = models.CharField(max_length=50)
    language = models.ForeignKey(Language)
    period = models.ForeignKey(Period)

class Topic(models.Model):
    image = models.ImageField(default='0011ff.png')
    periods = models.ManyToManyField(Period, related_name='periods')

    def get_periods(self):
        return "\n".join([p.id for p in self.periods.all()])

    def __str__(self):
        return str(self.id)

class TopicTr(models.Model):
    name = models.CharField(max_length=50)
    language = models.ForeignKey(Language)
    topic = models.ForeignKey(Topic)

class Content(models.Model):
    image = models.ImageField(default='0011ff.png')
    topic = models.ForeignKey(Topic)

    def __str__(self):
        return str(self.id)

class ContentTr(models.Model):
    language = models.ForeignKey(Language)
    content = models.ForeignKey(Content)
    title = models.TextField()
    text = models.TextField()