#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.views.generic import TemplateView

__author__ = 'rernande'

from django.conf.urls import url, include
from .views import dashboard, view_period, user, table, notifications, EditPeriodTrView, AddPeriodExtendedView, \
    RemovePeriodExtendedView, AddTopicExtendedView, EditTopicTrView, RemoveTopicExtendedView, \
    AddContentExtendedView, EditContentTrView, RemoveContentExtendedView, EditPeriodView


urlpatterns = [
    url(r'^$', dashboard, name = 'dashboard'),
    url(r'^period/(?P<period_id>\d+)/$', view_period, name = 'view_period'),  # Vue d'un
    url(r'^user/$', user, name = 'user'),
    url(r'^notifications/$', notifications, name = 'notifications'),
    url(r'^table/$', table, name = 'table'),

    url(r'^add_period_extended/$', AddPeriodExtendedView.as_view(), name = 'add_period_extended'),
    url(r'^add_period_extended_success/$', TemplateView.as_view(template_name='dashboard/add_period_extended_success.html'), name='add_period_extended_success'),
    url(r'^add_topic_extended/$', AddTopicExtendedView.as_view(), name='add_topic_extended'),
    url(r'^add_topic_extended_success/$', TemplateView.as_view(template_name='dashboard/add_topic_extended_success.html'), name='add_topic_extended_success'),
    url(r'^add_content_extended/$', AddContentExtendedView.as_view(), name='add_content_extended'),
    url(r'^add_content_extended_success/$', TemplateView.as_view(template_name='dashboard/add_content_extended_success.html'), name='add_content_extended_success'),

    url(r'^edit_period_tr/(?P<period_id>\d+)/(?P<language>\w+)/$', EditPeriodTrView.as_view(), name='edit_period_tr'),
    url(r'^edit_period_success/$', TemplateView.as_view(template_name='dashboard/edit_period_success.html'), name='edit_period_success'),
    url(r'^edit_topic_tr/(?P<topic_id>\d+)/(?P<language>\w+)/$', EditTopicTrView.as_view(), name='edit_topic_tr'),
    url(r'^edit_topic_success/$', TemplateView.as_view(template_name='dashboard/edit_topic_success.html'), name='edit_topic_success'),
    url(r'^edit_content_tr/(?P<content_id>\d+)/(?P<language>\w+)/$', EditContentTrView.as_view(), name='edit_content_tr'),
    url(r'^edit_content_success/$', TemplateView.as_view(template_name='dashboard/edit_content_success.html'), name='edit_content_success'),

    url(r'^remove_period_extended/(?P<pk>\d+)/$', RemovePeriodExtendedView.as_view(), name = 'remove_period_extended'),
    url(r'^remove_period_extended_success/$', TemplateView.as_view(template_name='dashboard/remove_period_extended_success.html'), name='remove_period_extended_success'),
    url(r'^remove_topic_extended/(?P<pk>\d+)/$', RemoveTopicExtendedView.as_view(), name = 'remove_topic_extended'),
    url(r'^remove_topic_extended_success/$', TemplateView.as_view(template_name='dashboard/remove_topic_extended_success.html'), name='remove_topic_extended_success'),
    url(r'^remove_content_extended/(?P<pk>\d+)/$', RemoveContentExtendedView.as_view(), name = 'remove_content_extended'),
    url(r'^remove_content_extended_success/$', TemplateView.as_view(template_name='dashboard/remove_content_extended_success.html'), name='remove_content_extended_success'),

    url(r'^edit_period/(?P<period_id>\d+)/$', EditPeriodView.as_view(), name='edit_period'),

]