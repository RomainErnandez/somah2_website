#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'rernande'

from django.conf.urls import url
from .views import dashboard, view_period, user, table, notifications

urlpatterns = [
    url(r'^$', dashboard, name = 'dashboard'),
    url(r'^period/(\d+)/$', view_period, name = 'view_period'),  # Vue d'un
    url(r'^user/$', user, name = 'user'),
    url(r'^notifications/$', notifications, name = 'notifications'),
    url(r'^table/$', table, name = 'table'),
]