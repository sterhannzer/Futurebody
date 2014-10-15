from django.conf.urls import patterns, url
from django.contrib import admin
from users.views import UsersIndex

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', UsersIndex.as_view(), name="user"),
)
