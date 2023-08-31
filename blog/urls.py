from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from blog import views
from users.apps import UsersConfig
from users.views import *

app_name = 'blog'

urlpatterns = ([
    path('', views.BlogListView.as_view(), name='blog_list'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))

