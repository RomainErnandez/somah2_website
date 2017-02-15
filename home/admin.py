from django.contrib import admin

from home.models import Language, Period, PeriodTr, Topic, TopicTr, Content, ContentTr


class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name', 'country',)

class PeriodAdmin(admin.ModelAdmin):
    # id needed because of order
    list_display = ('id', 'image',)

class PeriodTrAdmin(admin.ModelAdmin):
    list_display = ('period', 'name', 'language',)

class TopicAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'get_periods',)

class TopicTrAdmin(admin.ModelAdmin):
    list_display = ('name', 'language', 'topic_id',)

class ContentAdmin(admin.ModelAdmin):
    list_display = ('image', 'topic_id',)

class ContentTrAdmin(admin.ModelAdmin):
    list_display = ('language', 'content_id', 'title', 'text',)

# Register your models here.

admin.site.register(Language, LanguageAdmin)
admin.site.register(Period, PeriodAdmin)
admin.site.register(PeriodTr, PeriodTrAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(TopicTr, TopicTrAdmin)
admin.site.register(Content, ContentAdmin)
admin.site.register(ContentTr, ContentTrAdmin)