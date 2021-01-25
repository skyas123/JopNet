"""
Definition of urls for JopNet.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls import include, url
import JPT.views



urlpatterns = [
    url(r'^$',JPT.views.index, name='index'),
]
