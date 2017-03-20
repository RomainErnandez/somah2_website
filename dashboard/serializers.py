from rest_framework import serializers
from .models import Period, PeriodTr, Language


class PeriodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Period
        fields = ('id', 'image')

class PeriodTrSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeriodTr
        fields = ('period', 'language', 'name')

class TopicSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Period
        fields = ('id', 'image')

class TopicTrSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeriodTr
        fields = ('topic', 'language', 'name')

class ContentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Period
        fields = ('id', 'topic__id','image')

class ContentTrSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeriodTr
        fields = ('content', 'language', 'title', 'text')

class LanguageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Language
        fields = ('country', 'native_name')