from rest_framework import serializers

from .models import Period, PeriodTr, Language, ContentTr, Content, TopicTr, Topic


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
        model = Topic
        fields = ('id', 'image')

class TopicTrSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopicTr
        fields = ('topic', 'language', 'name')

class ContentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Content
        fields = ('id', 'topic_id','image')

class ContentTrSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentTr
        fields = ('content', 'language', 'title', 'text')

class LanguageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Language
        fields = ('country', 'native_name')

class AssociationPeriodTopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Period
        fields = ('id', 'periods')