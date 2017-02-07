from django.db import models
from django_countries.fields import CountryField

# Create your models here.

class Language(models.Model):
    name = models.CharField()
    country = CountryField(primary_key=True) # code: ISO 639-1

class Period(models.Model):
    image = models.ImageField()
    topics = models.ManyToManyField(Topic, related_name='topics')

class PeriodTr(models.Model):
    name = models.CharField()
    language = models.ForeignKey(Language)
    period = models.ForeignKey(Period)

class Topic(models.Model):
    # many to many with period ?
    image = models.ImageField()
    periods = models.ManyToManyField(Period, related_name='periods')

class TopicTr(models.Model):
    name = models.CharField()
    language = models.ForeignKey(Language)
    topic = models.ForeignKey(Topic)

class Content(models.Model):
    image = models.ImageField()
    topic = models.ForeignKey(Topic)

class ContentTr(models.Model):
    language = models.ForeignKey(Language)
    content = models.ForeignKey(Content)
    title = models.CharField()
    text = models.TextField()