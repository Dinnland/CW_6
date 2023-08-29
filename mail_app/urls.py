from django.conf.urls.static import static
from django.urls import path
# from django.contrib import admin
from django.conf import settings
from django.views.decorators.cache import cache_page

from .views import *


urlpatterns = [
    # 3
    path('base/', base),
    path('', HomeListView.as_view(extra_context={'title': 'DinnMail'}), name='home'),
    path('contacts/', index_contacts, name='contacts'),

    path('cabinet/', CabinetView.as_view(), name="cabinet"),
    # path('profile/', ProfileDataView.as_view(), name="profile"),

    path('create-mailing/', MailingCreateView.as_view(), name='mailing_create'),
    path('create-client/', ClientCreateView.as_view(), name='client_create'),
    path('create-mail/', MessageToMailingCreate.as_view(), name='mail_create'),
    #
    # 1
    path('mailinglist/', Mailing1ListView.as_view(extra_context={'title': 'DinnMail'}), name="mailinglist"),
    path('mailing/<int:pk>/update/', MailingUpdateView.as_view(), name='mailing_upd'),

    path('client/<int:pk>/update/', ClientUpdateView.as_view(), name='client_upd'),
    path('mail/<int:pk>/update/', MessageToMailingUpdateView.as_view(), name='client_upd'),

    # 1
    path('mailinglist/', Mailing1ListView.as_view(extra_context={'title': 'DinnMail'}), name="mailinglist"),

    path('client-list/', ClientListView.as_view(), name='client_list'),
    path('mail-list/', MailMessageListView.as_view(), name='mail_list'),
    path('mailing-log/<int:pk>', MailingLogsListView.as_view(), name='mailing_log'),
    path('all-mailing-log/<int:pk>', MailingLogsListView.as_view(), name='all_mailing_log'),

    path('mailing/<int:pk>/delete/', MailingDeleteView.as_view(), name='mailing_del'),
    path('client/<int:pk>/delete/', ClientDeleteView.as_view(), name='client_del'),
    path('mail/<int:pk>/delete/', MessageToMailingDeleteView.as_view(), name='mail_del'),
    path('update_status/<int:pk>/', MailingStatusUpdateView.as_view(), name='update_status'),

    path('not_authenticated/', NotAuthenticated.as_view(extra_context={'title': 'Dinnstore'}), name='not_authenticated'),

    path('moderka/', ModeratorViews.as_view(), name="moderators"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
