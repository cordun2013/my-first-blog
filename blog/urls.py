# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 20:56:53 2016

@author: catherineordun
"""

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]