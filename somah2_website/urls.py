"""somah2_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.views.static import serve
from rest_framework import routers

from dashboard.views import PeriodViewSet, PeriodTrViewSet, TopicViewSet, TopicTrViewSet, ContentViewSet, \
    ContentTrViewSet, LanguageViewSet, get_all_association_period_topic

router = routers.DefaultRouter()
router.register(r'periods', PeriodViewSet)
router.register(r'period_trs', PeriodTrViewSet)
router.register(r'topics', TopicViewSet)
router.register(r'topic_trs', TopicTrViewSet)
router.register(r'contents', ContentViewSet)
router.register(r'content_trs', ContentTrViewSet)
router.register(r'languages', LanguageViewSet)

urlpatterns = [
    # login, logout, password_change, password_change/done, password_reset, password_reset/done, reset/done
    url('^accounts/', include('django.contrib.auth.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^', include('dashboard.urls')),
    url(r'^api/association_period_topics', get_all_association_period_topic),
    url(r'^api/', include(router.urls)),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT,}),
]
