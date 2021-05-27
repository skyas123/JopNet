"""
Definition of urls for JopNet.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls import include, url
import JPT.views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    url(r'admin/',admin.site.urls),
    url(r'news',JPT.views.news, name='news'),
    url(r'^$',JPT.views.index, name='home'),
    url(r'friends',JPT.views.friends, name='friends'),
    url(r'^dialogs$',JPT.views.dialogs, name='dialogs'),
    url(r'^dialogs/(\d+)$',JPT.views.dialog, name='dialog'),
    url(r'auth',JPT.views.auth, name='auth'),
    url(r'^guest/(\d+)/(\d+)$',JPT.views.guest, name='guest'),
    url(r'registration',JPT.views.registration, name='registration'),
   # url(r'perInfo',JPT.views.perInfo, name='perInfo'),
    

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  #<- only for developing(probably)
