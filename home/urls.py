#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.views.generic import TemplateView

__author__ = 'rernande'

from django.conf.urls import url
from .views import dashboard, view_period, user, table, notifications, remove_period, EditPeriodExtendedView

urlpatterns = [
    url(r'^$', dashboard, name = 'dashboard'),
    url(r'^period/(?P<period_id>\d+)/$', view_period, name = 'view_period'),  # Vue d'un
    url(r'^user/$', user, name = 'user'),
    url(r'^notifications/$', notifications, name = 'notifications'),
    url(r'^table/$', table, name = 'table'),
    url(r'^remove_period/(?P<period_id>\d+)/$', remove_period, name = 'remove_period'),
    url(r'^edit_period_extended/(?P<period_id>\d+)/(?P<language>\w+)/$', EditPeriodExtendedView.as_view(), name='edit_period_extended'),
    url(r'^edit_period_extended_success/$', TemplateView.as_view(template_name='home/edit_period_extended_success.html'), name='edit_period_extended_success'),
]