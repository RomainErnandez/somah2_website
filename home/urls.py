#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'rernande'

from django.conf.urls import url
from .views import dashboard, view_period

urlpatterns = [
    url(r'^$', dashboard, name = 'dashboard'),
    url(r'^period/(\d+)/$', view_period, name = 'view_period'),  # Vue d'un
]