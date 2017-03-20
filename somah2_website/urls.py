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

from django.conf import settings
from rest_framework import routers

from dashboard.views import PeriodViewSet, PeriodTrViewSet, TopicViewSet, TopicTrViewSet, ContentViewSet, ContentTrViewSet, LanguageViewSet

router = routers.DefaultRouter()
router.register(r'periods', PeriodViewSet)
router.register(r'periodtrs', PeriodTrViewSet)
router.register(r'topics', TopicViewSet)
router.register(r'topictrs', TopicTrViewSet)
router.register(r'contents', ContentViewSet)
router.register(r'contenttrs', ContentTrViewSet)
router.register(r'languages', LanguageViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^dashboard/', include('dashboard.urls')),
    url(r'^api/', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)