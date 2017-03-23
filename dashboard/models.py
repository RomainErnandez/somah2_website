from django.contrib.auth.models import AbstractUser, User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_countries.fields import CountryField

# Create your models here.

class Language(models.Model):
    native_name = models.CharField(max_length=20)
    # country__code here https://fr.wikipedia.org/wiki/Liste_des_codes_ISO_639-1
    country = CountryField(primary_key=True)

    def __str__(self):
        return self.native_name

class Period(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True) # periods will be in id's order
    image = models.ImageField(default='0011ff.png')

    def __str__(self):
        return str(self.id)

class PeriodTr(models.Model):
    name = models.CharField(max_length=50)
    language = models.ForeignKey(Language)
    period = models.ForeignKey(Period)

    class Meta:
        unique_together = ('language', 'period',)

class Topic(models.Model):
    image = models.ImageField(default='0011ff.png')
    periods = models.ManyToManyField(Period, related_name='periods')

    def get_periods(self):
        return "\n".join([str(p.id) for p in self.periods.all()])

    def __str__(self):
        return str(self.id)

class TopicTr(models.Model):
    name = models.CharField(max_length=50)
    language = models.ForeignKey(Language)
    topic = models.ForeignKey(Topic)

    class Meta:
        unique_together = ('language', 'topic',)

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

    class Meta:
        unique_together = ('language', 'content',)

# https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='face-0.jpg')
    description = models.TextField(blank=True)
    company = models.CharField(max_length=50, blank=True, default='unknown')
    address = models.CharField(max_length=50, blank=True, default='unknown')
    postal_code = models.PositiveSmallIntegerField(blank=True)
    country = CountryField(blank=True)
    city = models.CharField(max_length=50, blank=True, default='unknown')

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
