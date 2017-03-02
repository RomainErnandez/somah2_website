#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'rernande'

from django.conf.urls import url
from .views import dashboard, view_period, user, table, notifications, remove_period, EditPeriodView

urlpatterns = [
    url(r'^$', dashboard, name = 'dashboard'),
    url(r'^period/(?P<period_id>\d+)/$', view_period, name = 'view_period'),  # Vue d'un
    url(r'^user/$', user, name = 'user'),
    url(r'^notifications/$', notifications, name = 'notifications'),
    url(r'^table/$', table, name = 'table'),
    url(r'^remove_period/(?P<period_id>\d+)/$', remove_period, name = 'remove_period'),
    url(r'^edit_period/$', EditPeriodView.as_view(), name='edit_period'),
]