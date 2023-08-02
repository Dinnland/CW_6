from django.urls import path
from django.contrib import admin


from .views import contact_view, success_view


# urlpatterns = [
#     path('', wiews.home, name='home'),
# ]
urlpatterns = [
    path('contact/', contact_view, name='contact'),
    path('success/', success_view, name='success'),
]