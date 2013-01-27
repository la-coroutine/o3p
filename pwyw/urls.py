from django.conf.urls import patterns, include, url

import views

urlpatterns = patterns('',
        url(r'^(?P<id>[\d]+)$', views.SplitView.as_view(), name='split'),
)
