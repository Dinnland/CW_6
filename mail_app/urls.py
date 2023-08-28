from django.conf.urls.static import static
from django.urls import path
from django.contrib import admin
from django.conf import settings

from .views import *


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]
