from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Language, Period, PeriodTr, Topic, TopicTr, Content, ContentTr, Profile


class LanguageAdmin(admin.ModelAdmin):
    list_display = ('native_name', 'country',)

class PeriodAdmin(admin.ModelAdmin):
    # id needed because of order
    list_display = ('id', 'image',)
    list_filter = ('id',)

class PeriodTrAdmin(admin.ModelAdmin):
    list_display = ('period', 'name', 'language',)
    readonly_fields = ('id',)
    list_filter = ('id', )

class TopicAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'get_periods',)

class TopicTrAdmin(admin.ModelAdmin):
    list_display = ('name', 'language', 'topic_id',)
    readonly_fields = ('id',)

class ContentAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'topic_id',)

class ContentTrAdmin(admin.ModelAdmin):
    list_display = ('language', 'content_id', 'title', 'text',)
    readonly_fields = ('id',)


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'


class ProfileAdmin(UserAdmin):
    inlines = (ProfileInline, )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'get_city')
    list_select_related = ('profile',)

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(ProfileAdmin, self).get_inline_instances(request, obj)

    def get_city(self, instance):
        return instance.profile.city
    get_city.short_description = 'City'

# Register your models here.

admin.site.register(Language, LanguageAdmin)
admin.site.register(Period, PeriodAdmin)
admin.site.register(PeriodTr, PeriodTrAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(TopicTr, TopicTrAdmin)
admin.site.register(Content, ContentAdmin)
admin.site.register(ContentTr, ContentTrAdmin)
admin.site.unregister(User)
admin.site.register(User, ProfileAdmin)