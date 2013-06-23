'''
    Created on Jun 22, 2013

    @author:  pgarnaut
'''

from django.conf.urls import patterns
import views

urlpatterns = patterns('',
    (r'^([0-9a-fA-F]+)[/]+$', views.index),
    (r'^$', views.index),
)